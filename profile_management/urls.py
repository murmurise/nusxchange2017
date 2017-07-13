# profile_management/urls
from django.conf.urls import url
from profile_management import views 

urlpatterns = [
	url(r'^', views.home, name='home'),
]