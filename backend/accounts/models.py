# -*- coding:utf-8 -*-
import binascii
import os
from django.db import models

from django.conf import settings  # upload path
from django_thumbs.db.models import ImageWithThumbsField

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
)


class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        '''
        Creates and saves a User with the given data
        '''
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=self.normalize_email(username),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self._create_user(username, password, **extra_fields)


class MyUser(AbstractBaseUser):
    MAIL = 1
    FEMAIL = 2
    GENDER_CHOICES = (
        (MAIL, u'男'),
        (FEMAIL, u'女'),
    )

    S_PENDING_REVIEW = 1
    S_NORMAL = 2
    S_BANNED = 9

    STATUS_CHOICES = (
        (S_PENDING_REVIEW, u'待审核'),
        (S_NORMAL, u'正常'),
        (S_BANNED, u'已禁用'),
    )

    FANS = 1
    ATHLETE = 2
    BOSS = 3

    ROLE_CHOICES = (
        (FANS, u'球迷'),
        (ATHLETE, u'运动员'),
        (BOSS, u'俱乐部老板'),
    )

    # basic info
    nick_name = models.CharField(u'昵称', max_length=256, blank=True, null=True)
    offical_name = models.CharField(u'真实姓名', max_length=256, blank=True, null=True)
    hide_offical_name = models.BooleanField(u'真实姓名保密', default=False)
    gender = models.IntegerField(u'性别', choices=GENDER_CHOICES, null=True, blank=True)
    avatar = ImageWithThumbsField(upload_to=settings.USER_AVATAR,
                                  default=settings.USER_AVATAR_DEFAULT,
                                  sizes=((200, 200), (450, 450)),
                                  verbose_name=u'头像')

    role = models.IntegerField(u'角色', choices=ROLE_CHOICES, default=FANS)
    status = models.IntegerField(u'状态', choices=STATUS_CHOICES, default=S_NORMAL)

    # 1. must have a single unique field that can be used for identification purposes
    # 2. provide a way to address the user in a “short” and “long” form
    username = models.CharField(u'用户名', max_length=32, unique=True, db_index=True)
    is_staff = models.BooleanField('系统管理员', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    # A list of the field names that will be prompted for when creating a user via the createsuperuser management command.
    REQUIRED_FIELDS = []

    @property
    def is_active(self):
        return self.status != self.S_BANNED

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name


class Token(models.Model):
    """authorization token model.

    不能同时登录多个账号
    """
    key = models.CharField(max_length=40, primary_key=True,
                           blank=True,  # create in admin
                           db_index=True)
    user = models.OneToOneField(MyUser, related_name='auth_token')
    user_agent = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'用户 Token'
        verbose_name_plural = verbose_name

    @classmethod
    def relogin(cls, user, user_agent):
        cls.logout(user)
        return cls.objects.create(user=user, user_agent=user_agent)

    @classmethod
    def logout(cls, user):
        try:
            user.auth_token.delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def get_user(cls, token):
        try:
            obj = cls.objects.get(token=token)
        except cls.DoesNotExist:
            return None
        return obj.user

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
        return '%s-%s' % (self.user, self.key)
