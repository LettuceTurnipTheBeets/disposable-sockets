# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0002_delete_integervalue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('time',)},
        ),
    ]
