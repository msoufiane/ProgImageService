from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from ProgImageService.settings.base import BASE_DIR
from repository.models import Image
import os


class ImageTest(TestCase):
    """Image model test case"""
    def tearDown(self):
        Image.objects.all().delete()

    def test_file_saved(self):
        """Given a valid file, it should be saved correctly"""
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        image = Image(file=imageFile)
        image.save()
        self.assertEqual(image.file.size, imageFile.size)  # check the saved file has the same size as the original
        self.assertTrue(image.pk > 0)

    def test_file_saved_exception(self):
        """Given an empty file, it should be raise an exception"""
        image = Image()

        try:
            image.full_clean()
            image.save()
        except Exception as e:
            self.assertTrue(isinstance(e, ValidationError))

        self.assertIsNone(image.pk)

    def test_file_retrieve(self):
        """Given a valid ID, it should return the correct file"""
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            originalImageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        savedImage = Image(file=originalImageFile)
        savedImage.full_clean()
        savedImage.save()
        savedImageID = savedImage.pk

        retrievedImage = Image.objects.get(pk=savedImageID)

        self.assertEqual(savedImage, retrievedImage)

    def test_file_retrieve_exception(self):
        """Given an invalid ID, it should raise an exception"""
        retrievedImage = None

        try:
            retrievedImage = Image.objects.get(pk=1)
        except Exception as e:
            self.assertTrue(isinstance(e, Image.DoesNotExist))

        self.assertIsNone(retrievedImage)
