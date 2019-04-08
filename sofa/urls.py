from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r"^admin/", admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^', include('sofas.urls')),
    url(r'^', include('about_us.urls')),
    url(r'^', include('guarantees.urls')),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
