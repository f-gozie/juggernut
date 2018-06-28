from django.conf.urls import url
from myregistration import views
from django.contrib.auth import views as auth_views


app_name = 'myregistration'
urlpatterns = [
	url(r'^register_vendor/', views.register_vendor, name='register_vendor'),
	url(r'^email_confirm/', views.email_confirm, name='email_confirm'),
	url(r'^password_change/$', views.password_change, name='password_change'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^login/', views.vendor_login, name='vendor_login'),
	url(r'^logout/', views.vendor_logout, name='vendor_logout'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]