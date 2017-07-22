# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'user_profile/home.html', {'user': user})