# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 15, 56, 25, 883204)),
        ),
        migrations.AlterField(
            model_name='room',
            name='duration',
            field=models.IntegerField(choices=[(1, '1 Hour'), (2, '6 Hours'), (3, '24 Hours')], default=3),
        ),
    ]
