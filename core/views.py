# core/views.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/lookup.html')

@login_required
def result(request):
    return render(request, 'core/result.html')