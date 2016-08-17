# -*- coding:utf-8 -*-
from django.conf.urls import url

from . import apis
from .models import MyUser

urlpatterns = (
    url(r'^login$', apis.login, name='user_api_login'),
    url(r'^logout$', apis.logout, name='user_api_logout'),
)
