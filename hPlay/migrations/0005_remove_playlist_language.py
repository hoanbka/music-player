# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-23 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hPlay', '0004_auto_20161023_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='language',
        ),
    ]
