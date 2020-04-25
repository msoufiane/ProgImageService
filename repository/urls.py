"""
in this file we config the urls with their respective views handlers
"""

from repository.views import save_image_view, retrieve_image_view
from django.urls import path

urlpatterns = [
    path('image', save_image_view, name='save_image'), # Upload image URL
    path('image/<int:id>', retrieve_image_view, name='retrieve_image'), # Retrieve image URL
]