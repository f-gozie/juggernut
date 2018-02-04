from django.conf.urls import url
from sweet import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]