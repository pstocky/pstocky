# -*- coding:utf-8 -*-
from rest_framework import generics  # noqa
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MyUser as User  # noqa
from .models import Token


@api_view(['POST'])
def login(request):
    """登录, 获取 token

    """
    return Response({
        'token': 'this is a token',
    })


@api_view(['GET'])
def logout(request):
    user = request.user
    if user.is_authenticated():
        Token.logout(user)
    return Response(status=status.HTTP_200_OK)
