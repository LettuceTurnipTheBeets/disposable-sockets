# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('message', models.TextField(max_length=140)),
                ('time', models.DateTimeField()),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True)),
                ('description', models.TextField(blank=True)),
                ('admin', models.CharField(max_length=20)),
                ('created', models.DateTimeField()),
                ('name', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='room',
            field=models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='sockets.Room'),
        ),
        migrations.AddField(
            model_name='chat',
            name='room',
            field=models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='sockets.Room'),
        ),
    ]
