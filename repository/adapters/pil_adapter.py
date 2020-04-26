"""
Django PIL implementation for images conversions
"""

from repository.types.image_converter import ImageConverter
from repository.utils import get_content_type_by_ext
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import File
from io import BytesIO
from PIL import Image

import logging
import os

logger = logging.getLogger(__name__)

class PILAdapter(ImageConverter):
    def convertImage(self, imageFile:File=None, ext:str=''):
        """saves the uploaded file to the disk and keeps the record of it in the DB"""
        if (not imageFile) or (not ext):
            return None
        
        try:
            originalImage = Image.open(imageFile.path)
            converted_file_io = BytesIO()
            originalImage.save(converted_file_io, format=ext)
            
            converted_file =  InMemoryUploadedFile(
                converted_file_io,
                None,
                '{}.{}'.format(os.path.splitext(imageFile.name)[0], ext),
                get_content_type_by_ext(ext),
                converted_file_io.tell,
                None
            )
            return converted_file
        except Exception as e:
            logger.error(e)
            return None