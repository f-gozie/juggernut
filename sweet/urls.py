from django.conf.urls import url
from sweet import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^vendor_index/', views.vendor_index, name='vendor_index'),
	url(r'^register_vendor/', views.register_vendor, name='register_vendor'),
	url(r'^login/', views.vendor_login, name='vendor_login'),
	url(r'^logout/', views.vendor_logout, name='vendor_logout'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
	
]