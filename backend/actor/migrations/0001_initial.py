# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, unique=True)),
                ('name', models.CharField(default=False, max_length=10)),
                ('phone', models.IntegerField()),
                ('idtype', models.CharField(default=b'IDCard', max_length=10)),
                ('idnum', models.CharField(unique=True, max_length=20)),
                ('isadult', models.BooleanField(default=True)),
                ('isman', models.BooleanField(default=True)),
                ('type', models.CharField(default=b'VIP', max_length=10)),
            ],
            options={
                'ordering': ('created',),
                'db_table': 'VIP',
            },
        ),
    ]
