# -*- coding:utf-8 -*-
import os
import json
import qiniu
import tempfile

from django.conf import settings

access_key = settings.QINIU_ACCESS_KEY
secret_key = settings.QINIU_SECRET_KEY
bucket_name = settings.QINIU_BUCKET_NAME
domain = settings.QINIU_BUCKET_CDN_DOMAIN

q = qiniu.Auth(access_key, secret_key)

policy = {
    'scope': bucket_name,
    'insertOnly': 1,
    'returnBody': json.dumps({
        'name': '$(fname)',
        'size': '$(fsize)',
        'key': '$(key)',
        'mimeType': '$(mimeType)',
        'hash': '$(etag)',
        # 'persistentId': '$(persistentId)',
    }),
    'fsizeLimit': 200 * 1024 * 1024,  # 200 MB
    'detectMime': 0,
    # 'mimeLimit': 'video/*',
}


def upload_file(file_stream, key):
    # seems that
    # qiniu do not support InMemoryFile upload very well

    # save file_stream to local tempfile
    with tempfile.NamedTemporaryFile(delete=False) as f:
        for chunk in file_stream.chunks():
            f.write(chunk)

    uptoken = q.upload_token(bucket=bucket_name, policy=policy)
    ret, info = qiniu.put_file(uptoken, key, f.name)
    # log ret
    os.unlink(f.name)
