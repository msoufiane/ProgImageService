"""
Django ORM implementation for ImageRepo interface

for example we can use another implementation such as storing and retrieving images from an AWS bucket
"""

from repository.types.image_repository import ImageRepo
from django.core.files import File
from repository.models import Image

import logging

logger = logging.getLogger(__name__)

class ORMAdapter(ImageRepo):
    def __init__(self):
        self.image_repo = Image

    def saveImage(self, imageFile:File=None):
        """
        saves the uploaded file to the disk and keeps the record of it in the DB
        """
        image_record = self.image_repo(file=imageFile)
        try:
            image_record.full_clean()
            image_record.save()
            return image_record.pk
        except Exception as e:
            logger.error(e)
            return 0

    def retrieveImage(self, id):
        """
        lookup an image file in the DB given it's ID (pk)
        """
        try:
            image_record = self.image_repo.objects.get(pk=id)
            return image_record
        except Image.DoesNotExist:
            logger.warn('No image record is found in the DB using id={}'.format(id))
            return None 
