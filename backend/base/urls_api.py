# -*- coding:utf-8 -*-
from django.conf.urls import include, url

urlpatterns = (
    url(r'^accounts/', include('accounts.urls_api')),
)
