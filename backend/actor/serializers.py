# -*- coding:utf-8 -*-
from rest_framework import serializers
from actor.models import Person


class partSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('created', 'name', 'phone', 'idtype', 'idnum', 'isadult','isman','type')
