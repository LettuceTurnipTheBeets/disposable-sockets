# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0009_remove_room_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
