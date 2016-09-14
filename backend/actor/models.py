# -*- coding:utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib import admin
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True,unique=True)
    name = models.CharField(max_length=10,)
    phone = models.IntegerField()
    IDcard = 1
    IDdrive = 2

    IDtype = (
        (IDcard, u'身份证'),
        (IDdrive, u'驾驶证'),
    )
    IDstatus = models.IntegerField(u'-请选择证件类型-', choices=IDtype, )

    idnum = models.CharField(max_length=20,unique=True,)

    Isadult = 1
    Notadult = 0

    Adultornot = (
        (Isadult, u'-成年-'),
        (Notadult, u'-未成年-'),
    )
    Adultor = models.IntegerField(u'-成年-', choices=Adultornot)


    man = 1
    woman =0
    isman =  (
        (man,u'男'),
        (woman,u'女')
    )
    sex = models.IntegerField(u'-性别-',choices=isman)

    VIP = 1
    normal =2
    admintype = (
        (normal,u'-普通会员-'),
        (VIP,u'-VIP会员-')
    )
    type = models.IntegerField(u'-请选择成员类型-',choices=admintype)

    class Meta:
        ordering = (u'created',)
        db_table = (u'VIP')
    def __str__(self):
        return self.name


admin.site.register(Person)