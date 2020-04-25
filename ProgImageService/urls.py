"""ProgImageService URL Configuration"""

from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('repository.urls')),
]