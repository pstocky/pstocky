# -*- coding:utf-8 -*-
import os
import hashlib
from django import forms
from django.contrib import admin

from .models import BookFile


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

        # upload to qiniu
        obj.qiniu_key = '%s_%s' % (obj.md5, obj.size_kb)

        # raw name and ext
        raw_filename = bookfile.name
        basename, ext = os.path.splitext(raw_filename)

        obj.filenames = basename
        obj.ext = ext

        if not obj.title:
            obj.title = basename

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

    list_display = (
        'title', 'language',
        'md5',
        'ext', 'size_kb',
    )

    list_filter = (
        'language',
        'ext',
    )

    search_fields = (
        'title',
        'filenames',
        'qiniu_key',
    )
