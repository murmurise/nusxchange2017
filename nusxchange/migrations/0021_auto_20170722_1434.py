# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusxchange', '0020_auto_20170722_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_picture/no-img.jpg', upload_to='profile_picture'),
        ),
    ]
