from django.conf.urls import url, include
from django.contrib import admin
from sofas import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [

    url(r'^sofas_(?P<sofa_id>\w+)/$', views.sofa, name='sofa'),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
