from django.conf.urls import url, include
from django.contrib import admin
from about_us import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [

    url(r'^about_us(?P<about_id>\w+)/$', views.about_us, name='about_us'),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)