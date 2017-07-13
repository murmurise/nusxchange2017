# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(_("age"))
# class User(models.Model):
# 	username = models.CharField(max_length = 250)
# 	password = models.CharField(max_length = 250)
# 	nickname = models.CharField(max_length = 250)
# 	matric_num = models.CharField(max_length = 250)
# 	age = models.CharField(max_length = 250)
# 	gender = models.CharField(max_length = 250)
# 	major = models.CharField(max_length = 250)
# 	nationality = models.CharField(max_length = 250)
# 	interest = models.CharField(max_length = 250)
# 	photo = models.CharField(max_length = 250)
# 	facebook_url = models.CharField(max_length = 250)