from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from repository.adapters.orm_adapter import ORMAdapter
from ProgImageService.settings.base import BASE_DIR
import os

class ORMAdapterTest(TestCase):
    """orm adapter test case"""
    def test_save_image_working(self):
        adapter = ORMAdapter()
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
            id = adapter.saveImage(imageFile=imageFile)
            self.assertGreater(id, 0)
    
    def test_save_image_exception(self):
        adapter = ORMAdapter()
        id = adapter.saveImage(imageFile=None)
        self.assertEqual(id, 0)

    def test_retrieve_image_working(self):
        adapter = ORMAdapter()
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
            id = adapter.saveImage(imageFile=imageFile)
            self.assertNotEqual(adapter.retrieveImage(id=id), None)

    def test_retrieve_image_exception(self):
        adapter = ORMAdapter()
        self.assertEqual(adapter.retrieveImage(id=999), None)

