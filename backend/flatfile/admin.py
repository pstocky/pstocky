# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import BookFile


@admin.register(BookFile)
class BookFileAdmin(admin.ModelAdmin):
    list_display = (
        'md5',
        'title', 'language',
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
