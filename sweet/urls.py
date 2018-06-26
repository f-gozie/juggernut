from django.conf.urls import url
from sweet import views
from django.contrib.auth import views as auth_views


app_name = 'sweet'
urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^vendor_index/', views.vendor_index, name='vendor_index'),
]