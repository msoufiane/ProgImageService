from rest_framework import status

from django.test import TestCase, Client
from django.urls import reverse

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from ProgImageService.settings.base import BASE_DIR
from repository.models import Image

import ast
import os
import io

client = Client()

class ImageViewTest(TestCase):
    """Image View test case"""

    def test_retrieve_image_working(self):
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        image = Image(file=imageFile)
        image.save()

        response = client.get(reverse('retrieve_image', kwargs={'id': image.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as originalFile:
            self.assertEquals(response.content, originalFile.read())

    
    def test_retrieve_image_not_found(self):
        """Given an empty file, it should be raise an exception"""
        response = client.get(reverse('retrieve_image', kwargs={'id': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_save_image_workning(self):
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            response = client.post(reverse('save_image'), {'image': testFile})  
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            responseDict = ast.literal_eval(response.content.decode('utf8'))
            self.assertGreater(responseDict['id'], 0)

    def test_save_image_badrequest_if_bad_or_no_file(self):
        response = client.post(reverse('save_image'))  
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            response2 = client.post(reverse('save_image'), {'bad_key': testFile})  
            self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_save_image_badrequest_if_file_not_image(self):
        with open(os.path.join(BASE_DIR, '..', 'fixtures/files/file1.pdf'), 'rb') as testFile:
            response = client.post(reverse('save_image'), {'image': testFile})  
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
