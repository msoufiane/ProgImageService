"""
Various helper functions
"""

from django.core.files.base import File
from repository.settings import SUPPORTED_IMAGES

import logging
import magic
import os

logger = logging.getLogger(__name__)

def image_is_valide(image:File=None):
    """check the image content_type agains the SUPPORTED_IMAGES config"""
    if not image.content_type in SUPPORTED_IMAGES:
        return False
    return True

def get_content_type(filePath:str):
    """return the MIME Type from a file given it's path"""
    mime = magic.Magic(mime=True)
    try:
        mime_type = mime.from_file(filePath)
        return mime_type
    except Exception as e:
        logger.error(e) 
        raise e

def delete_file(filePath=None):
   """ Deletes a file from the filesystem given it's path"""
   try:
       os.remove(filePath)
   except Exception as e:
       logger.error(e)
       raise e