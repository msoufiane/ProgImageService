from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from repository.adapters.orm_adapter import ORMAdapter
from repository.adapters.pil_adapter import PILAdapter
from repository.utils import get_content_type_by_ext
from ProgImageService.settings.base import BASE_DIR

import os


class ORMAdapterTest(TestCase):
    """ORM Adapter test case"""

    def test_save_image_working(self):
        """Given a valid file, an image record should be created in the DB"""
        adapter = ORMAdapter()
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
            id = adapter.saveImage(imageFile=imageFile)
            self.assertGreater(id, 0)

    def test_save_image_exception(self):
        """Given an invalid file, the image record shouldn't be created in the DB and a 0 is returned"""
        adapter = ORMAdapter()
        id = adapter.saveImage(imageFile=None)
        self.assertEqual(id, 0)

    def test_retrieve_image_working(self):
        """Given a valid ID, an image record should be found in the DB"""
        adapter = ORMAdapter()
        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
            id = adapter.saveImage(imageFile=imageFile)
            self.assertNotEqual(adapter.retrieveImage(id=id), None)

    def test_retrieve_image_exception(self):
        """Given an invalid ID, the image record shouldn't be found in the DB and a `None` is returned"""
        adapter = ORMAdapter()
        self.assertEqual(adapter.retrieveImage(id=999), None)


class PILAdapterTest(TestCase):
    """PIL Adapter test case"""

    def test_image_converted(self):
        """Given a valid file, it should be converted correctly"""
        adapter = PILAdapter()
        orm_adapter = ORMAdapter()
        EXT = 'png'

        with open(os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg'), 'rb') as testFile:
            imageFile = SimpleUploadedFile(name=testFile.name, content=testFile.read())
            record_id = orm_adapter.saveImage(imageFile)

            original_image = orm_adapter.retrieveImage(record_id)
            converted_image = adapter.convertImage(original_image.file, EXT)

            self.assertEqual(
                converted_image.content_type,
                get_content_type_by_ext(EXT)
            )

    def test_convert_image_none_file(self):
        """Given a None file to convert, we should get a None back"""
        adapter = PILAdapter()
        EXT = 'png'
        converted_image = adapter.convertImage(None, EXT)
        self.assertIsNone(converted_image)

    def test_convert_unsupported_para(self):
        """Given an unsupported param, we should get a None back"""
        adapter = PILAdapter()
        EXT = 'png'
        converted_image = adapter.convertImage('STRING_PARAM', EXT)
        self.assertIsNone(converted_image)
