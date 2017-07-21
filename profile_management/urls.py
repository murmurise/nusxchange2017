# profile_management/urls
from django.conf.urls import url
from profile_management import views 

urlpatterns = [
	url(r'^$', views.get_summary, name='myhome'),
	url(r'^settings/', views.edit_profile, name='settings')
]