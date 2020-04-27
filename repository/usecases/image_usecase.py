"""
image repository usecase
business logic is implemented here
"""

from repository.types.image_converter import ImageConverter
from repository.types.image_repository import ImageRepo
from django.core.files.base import File

import inject
import logging

logger = logging.getLogger(__name__)


class ImageNotFoundError(Exception):
    pass


class ImageUseCase(object):
    @inject.autoparams('image_repo', 'image_converter')
    def __init__(self, image_repo: ImageRepo, image_converter: ImageConverter):
        self._image_repo = image_repo
        self._image_converter = image_converter

    def save_image(self, imageFile: File = None):
        if not imageFile:
            return 0

        imageID = self._image_repo.saveImage(imageFile)
        return imageID

    def retrieve_image(self, id: int):
        image = self._image_repo.retrieveImage(id)
        if not image:
            raise ImageNotFoundError
        return image

    def convert_image(self, imageFile: File = None, ext: str = ''):
        return self._image_converter.convertImage(imageFile, ext)
