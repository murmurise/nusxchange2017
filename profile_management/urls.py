# profile_management/urls
from django.conf.urls import url
from profile_management import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.get_summary, name='myhome'),
	url(r'^settings/', views.edit_profile, name='settings')
]