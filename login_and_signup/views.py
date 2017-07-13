# login_and_signup/views
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login

from django.views import generic
from django.views.generic import View
from login_and_signup.forms import  UserCreationForm

# @login_required
def home(request):
    return render(request, 'login_and_signup/home.html')

def login(request):
    auth_login(request)
    return render(request, 'profile_management/home.html')

# after logging in, user is redirected to the settings page
def loggedin (request):
    return redirect('http://localhost:8000/settings/')

# class UserFormView(View):
# 	form_class = UserForm
# 	template_name = 'login_and_signup/newaccount.html'

# 	def get(self, request):
# 		form = self.form_class(None)
# 		return render (request, self.template_name, {'form': form})

# 	def post(self, request):
# 		form = self.form_class(request.POST)

# 		if form.is_valid():
# 			user = form.save(commit=False)

# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']
# 			nickname = form.cleaned_data['password']
# 			matric_num = form.cleaned_data['password']
# 			age = form.cleaned_data['password']
# 			gender = form.cleaned_data['password']
# 			major = form.cleaned_data['password']
# 			nationality = form.cleaned_data['password']
# 			interest = form.cleaned_data['password']
# 			# photo = models.CharField(max_length = 250)
# 			# facebook_url = models.CharField(max_length = 250)
# 			user.set_password(password)#to change password
# 			user.save()

# 			#returns user objects if credentials are correct
# 			user = authenticate (username = username, password = password)
# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return redirect('http://localhost:8000/settings')

# 		return render (request, self.template_name, {'form': form})

    
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
    
def signup(request):
    logout(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            age = form.cleaned_data.get('age')
            user = authenticate(username=username, password=raw_password)
            return login(request)
    else:
        form = UserCreationForm()
    return render(request, 'login_and_signup/newaccount.html', {'form': form})
