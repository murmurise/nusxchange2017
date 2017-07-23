# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    soc = 1
    fass = 2
    fos = 3
    biz = 4
    dent = 5
    sde = 6
    duke = 7
    eng = 8
    law = 9
    med = 10
    music = 11
    sph = 12
    spp = 13
    yale = 14
    oth = 15
    SCHOOL_CHOICES = (
        (soc, 'School of Computing'),
        (fass, 'Faculty of Arts & Social Science'),
        (fos, 'Faculty of Science'),
        (biz, 'Business and Accountancy'),
        (dent, 'Dentistry'),
        (sde, 'Design & Environment'),
        (duke, 'Duke-NUS'),
        (eng, 'Engineering'),
        (law, 'Law'),
        (med, 'Medicine'),
        (music, 'Music'),
        (sph, 'Public Health'),
        (spp, 'Public Policy'),
        (yale, 'Yale-NUS'),
        (oth, 'Others'),
        )
    TEMASEK='TH'
    EUSOFF='EH'
    CINNAMON='CC'
    TEMBUSU='TC'
    OFFCAMPUS='OC'
    ACCOMODATION_CHOICES = (
        (TEMASEK, 'Temasek Hall'),
        (EUSOFF, 'Eusoff Hall'),
        (CINNAMON, 'Cinnamon College'),
        (TEMBUSU, 'Tembusu College'),
        (OFFCAMPUS, 'Off-Campus')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, null = False, blank=True )
    accomodation = models.CharField(
        max_length=2, 
        blank=False, 
        default = OFFCAMPUS,
        choices = ACCOMODATION_CHOICES,
        )
    birth_date = models.DateField(null=True, blank=False)
    school = models.PositiveSmallIntegerField(
        choices = SCHOOL_CHOICES, 
        blank = False,
        default = oth,
        )
    nickname = models.CharField(max_length=30, null=False, blank=True)
    matric_num = models.CharField(
        max_length=9, 
        blank=False, 
        default = 'A0000000Z',)
    age = models.CharField(max_length=3, blank=False, default=18)

    gender = models.CharField(
        max_length=3, 
        choices = (('F', 'Female'),('M', 'Male'),), 
        default='M',
        )
    major = models.CharField(max_length=30, null = False, blank=True)
    

    NATIONALITY_CHOICES=(
        ('CN',  'China'),
        ('SG', 'Singapore'),
        ('OT', 'Others'),
        ) #tbc
    nationality = models.CharField(
        choices = NATIONALITY_CHOICES,
        max_length=2, 
        blank=False, 
        default='OT',
        )
    interest = models.CharField(max_length=300, null = False, blank=True)
    university = models.CharField(max_length=300, null = False, blank = True)
    facebook_url = models.URLField(null = False, blank=True, )
    profile_picture = models.ImageField(
        upload_to="profile_picture", 
        blank=False, 
        null = False, 
        default="profile_picture/no-img.jpg",
        )

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

class ProfileForm (ModelForm):
    class Meta:
        model = Profile
        fields = [
        'user', 
        'bio',
        'accomodation',
        'birth_date', 
        'school', 
        'nickname', 
        'matric_num', 
        'age', 
        'gender', 
        'major', 
        'nationality',
        'interest',
        'profile_picture',
        'facebook_url',
        'university',
        ]
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

# https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
# What we want to achieve is making the fields location, birthdate and role available to be edited on Django Admin.
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()   