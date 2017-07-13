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

def post(self, request):
	form = self.form_class(request.POST)

	if form.is_valid():
		user = form.save(commit=False)

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		nickname = form.cleaned_data['password']
		matric_num = form.cleaned_data['password']
		age = form.cleaned_data['password']
		gender = form.cleaned_data['password']
		major = form.cleaned_data['password']
		nationality = form.cleaned_data['password']
		interest = form.cleaned_data['password']
		# photo = models.CharField(max_length = 250)
		# facebook_url = models.CharField(max_length = 250)
		user.set_password(password)#to change password
		user.save()


	return redirect('http://localhost:8000/settings')


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
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })