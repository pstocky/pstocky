# -*- coding:utf-8 -*-
import os
import hashlib
from django import forms
from django.contrib import admin

from .models import BookFile
from utils.uploads import upload_file

from django.conf import settings


qiniu_domain = settings.QINIU_BUCKET_CDN_DOMAIN


class BookFileCreationForm(forms.ModelForm):
    """A form for creating new BookFile.

    calculate md5 / size / ext automatically
    """
    bookfile = forms.FileField(label=u'语言')
    title = forms.CharField(label=u'书名', required=False)

    class Meta:
        model = BookFile
        fields = (
            'bookfile',
            'language',
            'title',
            'desc',
        )

    def clean_bookfile(self):
        bookfile = self.cleaned_data['bookfile']

        # calc md5_obj
        md5_obj = hashlib.md5()
        for chunk in bookfile.chunks():
            md5_obj.update(chunk)
        md5 = md5_obj.hexdigest()

        try:
            BookFile.objects.get(md5=md5)
        except BookFile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError(u'file exists')
        return bookfile

    def save(self, commit=True):
        bookfile = self.cleaned_data['bookfile']

        # calc md5_obj
        md5_obj = hashlib.md5()
        for chunk in bookfile.chunks():
            md5_obj.update(chunk)
        md5 = md5_obj.hexdigest()

        obj = super(BookFileCreationForm, self).save(commit=False)
        obj.md5 = md5
        # size, set to 1 if less than 1
        obj.size_kb = bookfile.size / 1024 or 1

        # raw name and ext
        raw_filename = bookfile.name
        basename, ext = os.path.splitext(raw_filename)

        obj.filenames = basename
        obj.ext = ext

        if not obj.title:
            obj.title = basename

        # upload to qiniu
        obj.qiniu_key = obj.gen_qiniu_key()
        # TODO: upload async. use celery
        upload_file(bookfile, obj.qiniu_key)

        if commit:
            obj.save()
        return obj


@admin.register(BookFile)
class BookFileAdmin(admin.ModelAdmin):
    # The forms to add and change BookFile instances
    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return BookFileCreationForm
        return super(BookFileAdmin, self).get_form(request, obj, **kwargs)

    def download_url(self, ins):
        return '<a href="%s/%s">%s</a>' % (
            qiniu_domain, ins.qiniu_key, ins.title)

    download_url.short_description = u"下载链接"
    download_url.allow_tags = True

    readonly_fields = (
        'download_url',
    )

    list_display = (
        'title', 'language',
        'md5',
        'ext', 'size_kb',
        'download_url',
        'checked',
    )

    list_filter = (
        'language',
        'ext',
        'ad_inside', 'incomplete', 'not_clear',
        'checked',
    )

    search_fields = (
        'title',
        'filenames',
        'qiniu_key',
    )
