from django.urls import path
from repository.views.image_views import save_image, retrieve_image

urlpatterns = [
    path('image', save_image, name='save_image'),
    path('image/<int:id>', retrieve_image, name='retrieve_image'),
]