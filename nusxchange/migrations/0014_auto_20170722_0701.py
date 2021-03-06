# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusxchange', '0013_auto_20170721_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pu',
            field=models.CharField(default='National Univeristy of Singapore', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.PositiveSmallIntegerField(choices=[(1, 'School of Computing'), (2, 'Faculty of Arts & Social Science'), (3, 'Faculty of Science'), (4, 'Business and Accountancy'), (5, 'Dentistry'), (6, 'Design & Environment'), (7, 'Duke-NUS'), (8, 'Engineering'), (9, 'Law'), (10, 'Medicine'), (11, 'Music'), (12, 'Public Health'), (13, 'Public Policy'), (14, 'Yale-NUS'), (15, 'Others')], default=15),
        ),
    ]
