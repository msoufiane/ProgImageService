from repository.types.image_repository import ImageRepo
from django.core.files import File
from repository.models import Image

import logging

logger = logging.getLogger(__name__)

class ORMAdapter(ImageRepo):
    def __init__(self):
        self.image_repo = Image

    def saveImage(self, imageFile:File=None):
        image_record = self.image_repo(file=imageFile)
        try:
            image_record.full_clean()
            image_record.save()
            return image_record.pk
        except Exception as e:
            logger.fatal(e)
            return 0

    def retrieveImage(self, id):
        try:
            image_record = self.image_repo.objects.get(pk=id)
            return image_record
        except Image.DoesNotExist:
            return None 
