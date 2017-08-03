# signup/views
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from signup.forms import  SignUpForm
from django.contrib.auth import login as auth_login
from django.views.generic import View
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()# load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('/me')
    else:
        form = SignUpForm()
    return render(request, 'signup/index.html', {'form': form})
    # return render(request, 'signup/newaccount.html', {'form': form})

