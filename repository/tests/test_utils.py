from django.test import TestCase
from repository.utils import delete_file
from ProgImageService.settings.base import BASE_DIR, MEDIA_ROOT

from shutil import copy2
import os

class UtilsTest(TestCase):
    """Utility methods test case"""

    def test_delete_file(self):
        """Given a valid file path, it should be deleted correctly"""
        original_file =  os.path.join(BASE_DIR, '..', 'fixtures/images/image1.jpeg')
        dummy_file = os.path.join(MEDIA_ROOT, 'uploads/car1.jpeg')

        copy2(original_file, dummy_file)

        delete_file(dummy_file)
        self.assertFalse(os.path.isfile(dummy_file))
 
    def test_exception_when_invalid_file(self):
        """Should raise an exception when giving an invalid file path"""
        self.assertRaises(TypeError, delete_file, path=None)
