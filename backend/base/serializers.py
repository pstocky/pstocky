# -*- coding:utf-8 -*-
from rest_framework import serializers


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj][1]

    def to_internal_value(self, data):
        for idx, value in self._choices:
            if value == data:
                return idx
