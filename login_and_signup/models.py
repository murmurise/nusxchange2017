# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # nickname = models.CharField(max_length=30, blank=True)
	# matric_num = models.CharField(max_length=30, blank=True)
	# age = models.CharField(max_length=30, blank=True)
	# gender = models.CharField(max_length=30, blank=True)
	# major = models.CharField(max_length=30, blank=True)
	# nationality = models.CharField(max_length=30, blank=True)
	# interest = models.CharField(max_length=30, blank=True)
	# photo = models.CharField(max_length=30, blank=True)
	# facebook_url = models.CharField(max_length=30, blank=True)

#define signals so our Profile model will be automatically created/updated 
# when we create/update User instances.hooking the create_user_profile and 
# save_user_profile methods to the User model, whenever a save event occurs
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()