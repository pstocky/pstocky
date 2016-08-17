# -*- coding:utf-8 -*-
from random import choice
from string import ascii_lowercase, digits

from django.contrib.auth import get_user_model


def generate_random_username(length=16,
                             chars=ascii_lowercase + digits,
                             split=4,
                             delimiter='-'):

    UserModel = get_user_model()
    username = ''.join([choice(chars) for i in xrange(length)])

    if split:
        username = delimiter.join([
            username[start:start + split]
            for start in range(0, len(username), split)])

    try:
        UserModel._default_manager.get_by_natural_key(username)
        return generate_random_username(length=length, chars=chars,
                                        split=split, delimiter=delimiter)
    except UserModel.DoesNotExist:
        return username
