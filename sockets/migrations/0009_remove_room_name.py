# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0008_auto_20170905_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
    ]
