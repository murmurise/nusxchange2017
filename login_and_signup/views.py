# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
# Create your views here.

@login_required
def home(request):
    return render(request, 'login_and_signup/home.html')

# def login(request):
#     return render(request, 'login_and_signup/login.html')

class UserFormView(View):
	form_class = UserForm
	template_name = 'login_and_signup/newaccount.html'

	def get(self, request):
		form = self.form_class(None)
		return render (request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)#to change password
			user.save()

			#returns user objects if credentials are correct
			user = authenticate (username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('login_and_signup:home')

		return render (request, self.template_name, {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
