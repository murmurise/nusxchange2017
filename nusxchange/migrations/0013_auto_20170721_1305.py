# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusxchange', '0012_auto_20170721_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.PositiveSmallIntegerField(choices=[(1, 'School of Computing'), (2, 'Faculty of Arts & Social Science'), (3, 'Faculty of Science'), (4, 'Business and Accountancy'), (5, 'Dentistry'), (6, 'Design & Environment'), (7, 'Duke-NUS'), (8, 'Engineering'), (9, 'Law'), (10, 'Medicine'), (11, 'Music'), (12, 'Public Health'), (13, 'Public Policy'), (3, 'Science'), (14, 'Yale-NUS'), (15, 'Others')], default=15),
        ),
    ]