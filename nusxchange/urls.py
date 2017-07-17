# nusxchange/urls
"""nusxchange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login_and_signup import views as core_views
from profile_management import views as profile_view

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    # url(r'^login/', include('login_and_signup.urls')),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/', include('login_and_signup.urls', namespace='login')),
    url(r'^signup/', include('signup.urls', namespace='signup')),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^settings/', include('profile_management.urls', namespace='settings')),
    # url(r'^profile/',include()) #profile of other users
    # url(r'^core/',) #core app for looking up other users
    # url(r'^home/',) #intro to the app
    url(r'^accounts/profile/', profile_view.home, name = 'home') 

]
