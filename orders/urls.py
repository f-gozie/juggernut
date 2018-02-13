from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.create_order, name='create_order'),
]
# Still don't know what to put here