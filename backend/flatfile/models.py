# -*- coding:utf-8 -*-
from django.db import models

from django.conf import settings


class BookFile(models.Model):

    CHINESE = 'cn'
    ENGLISH = 'en'
    LANGUAGE_CHOICES = (
        (CHINESE, u'中文'),
        (ENGLISH, u'English'),
    )

    md5 = models.CharField(u'MD5', max_length=32, primary_key=True)
    qiniu_key = models.CharField(u'七牛 key', max_length=100, unique=True)

    title = models.CharField(u'书名', max_length=100, db_index=True)
    filenames = models.CharField(u'原始文件名', max_length=100)

    ext = models.CharField(u'扩展名', max_length=100)
    size_kb = models.PositiveIntegerField(u'大小(KB)')
    language = models.CharField(u'语言', max_length=10, choices=LANGUAGE_CHOICES)

    # quality
    ad_inside = models.BooleanField(u'内含广告', default=True)
    incomplete = models.BooleanField(u'内容残缺', default=True)
    not_clear = models.BooleanField(u'扫描不清晰', default=True)

    checked = models.BooleanField(u'已校验', default=False)
    checker = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'校验人', null=True, blank=True)

    desc = models.TextField(u'描述', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = u'电子书文件'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def gen_qiniu_key(self):
        return '%s_%s%s' % (self.md5, self.size, self.ext)
