from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from sweet import views

urlpatterns = [
    url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^orders/', include('orders.urls')),
    url(r'^', include('myregistration.urls')),
	url(r'^', include('sweet.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# url(r'^cart/', include('cart.urls')),     