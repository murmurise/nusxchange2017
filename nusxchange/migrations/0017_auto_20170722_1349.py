# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusxchange', '0016_auto_20170722_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media/profile_picture/no-img.jpg', upload_to='media/profile_picture'),
        ),
    ]