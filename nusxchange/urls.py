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
from login_and_signup import views as login_views
from profile_management import views as profile_view
from django.conf import settings
from django.conf.urls.static import static
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    url(r'^$', login_views.home, name='home'), #intro page
    url(r'^login/', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True, 'template_name': 'login_and_signup/login.html'} ), #login page
    url(r'^signup/', include('signup.urls', namespace='signup')), #sign up page
    url(r'^logout/$', login_views.logout, name='logout'), #logout and redirect to the intro page
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^me/', include('profile_management.urls', namespace = 'profile')),
    url(r'^profile/', include('user_profile.urls')), #to visit others' profiles
    url(r'^core/', include('core.urls', namespace='core')), #search users by categories
    url(r'^admin/', admin.site.urls), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
