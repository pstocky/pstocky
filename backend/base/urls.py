# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from actor import views

urlpatterns = patterns('',  # noqa
    url(r'^$', 'base.views.home', name='home'),
    url(r'^api$', 'base.views.api_home', name='api_home'),
    url(r'^api/', include('base.urls_api')),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^Actor_API/$', views.allnumber),
    url(r'^Actor_API/(?P<pk>[0-9]+)$', views.number),
)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]



if settings.DEBUG:
    urlpatterns += patterns('',  # noqa
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,
             }
            ),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT,
             }
            ),
        url(r'^vivian/(?P<template_name>.*)$', 'base.views.vivian'),
    )
