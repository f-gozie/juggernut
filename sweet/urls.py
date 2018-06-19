from django.conf.urls import url
from sweet import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^register_vendor/', views.register_vendor, name='register_vendor')
	
]