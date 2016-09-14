# -*- coding:utf-8 -*-

# Create your models here.
# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib import admin
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True,unique=True)
    name = models.CharField(max_length=10,default='参加者姓名')
    phone = models.IntegerField(default='11位手机号码')
    IDcard = 1
    IDdrive = 2

    IDtype = (
        (IDcard, u'身份证'),
        (IDdrive, u'驾驶证'),
    )
    IDstatus = models.IntegerField(u'-请选择证件类型-', choices=IDtype, default=IDcard)

    idnum = models.CharField(max_length=20,unique=True,default='证件号码')

    Isadult = 1
    Notadult = 0

    Adultornot = (
        (Isadult, u'-成年-'),
        (Notadult, u'-未成年-'),
    )
    Adultor = models.IntegerField(u'-成年-', choices=Adultornot, default=Isadult)


    man = 1
    woman =0
    isman =  (
        (man,u'男'),
        (woman,u'女')
    )
    sex = models.IntegerField(u'-性别-',choices=isman,default=man)

    VIP = 1
    normal =2
    admintype = (
        (normal,u'-普通会员-'),
        (VIP,u'-VIP会员-')
    )
    type = models.IntegerField(u'-请选择成员类型-',choices=admintype,default=normal)

    class Meta:
        ordering = ('created',)
        db_table = ('VIP')
    def __str__(self):
        return self.name


admin.site.register(Person)