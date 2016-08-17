# -*- coding:utf-8 -*-
import socket

from django.template.response import TemplateResponse
from django_redis import get_redis_connection
from rest_framework.decorators import api_view
from rest_framework.response import Response

redis = get_redis_connection("default")
host = socket.gethostname()


@api_view(['GET'])
def api_home(request):
    key = 'test:hits'
    redis.incr(key)
    return Response('Hello World!'
                    'I have been seen %s times.'
                    'My Host name is %s.' % (redis.get(key), host))


def home(request,
         template_name='home.html'):
    key = 'test:hits'
    redis.incr(key)

    context = {
        'hits': redis.get(key),
        'hostname': host,
    }
    return TemplateResponse(request, template_name, context)


def vivian(request, template_name='home.html'):
    return TemplateResponse(request, template_name)
