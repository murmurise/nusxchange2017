# profile_management/views

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login_and_signup.forms import UserForm, ProfileForm
from django.contrib import messages


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile:myhome')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(
        request, 'profile_management/settings.html', 
        {'user_form': user_form,'profile_form': profile_form}
        )

@login_required
def get_summary(request):
    return render(request, 'profile_management/home.html')