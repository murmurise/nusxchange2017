# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nusxchange', '0021_auto_20170722_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='pu',
            new_name='university',
        ),
    ]