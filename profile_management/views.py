# profile_management/views

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'profile_management/setting.html')


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile:settings')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_management/settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })