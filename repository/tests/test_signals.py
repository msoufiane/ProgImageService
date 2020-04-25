from repository.models import Image
from repository.signals import delete_imageFile
from ProgImageService.settings.base import BASE_DIR
from django.db.models.signals import post_delete, ModelSignal
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from unittest import mock
import os

class SignalsTest(TestCase):
    """Sigmalss test case"""

    @mock.patch('repository.signals.delete_imageFile')
    def test_post_delete_signal(self, mock):
        """On deleting an Image mode, the post_delete signal should be called once"""

        post_delete.connect(mock.handler, sender=Image)
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        image = Image(file=imageFile)
        image.save()
        image.delete()

        self.assertTrue(mock.handler.called)
        self.assertEqual(mock.handler.call_count, 1)

    def test_image_file_is_deleted(self):
        """Tests the signal method actually delete the file"""
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        image = Image(file=imageFile)
        image.save()

        delete_imageFile(sender=Image, instance=image)
        self.assertFalse(os.path.isfile(image.file.path))

    def test_exception_if_file_not_found(self):
        """Tests the signal method actually delete the file"""
        with open(os.path.join(BASE_DIR, '..' , 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
        image = Image(file=imageFile)
        image.save()
        image.delete()

        self.assertRaises(FileNotFoundError, delete_imageFile, sender=Image, instance=image)