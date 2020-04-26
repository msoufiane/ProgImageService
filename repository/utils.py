"""
Various helper functions
"""

from django.core.files.base import File
from repository.settings import SUPPORTED_IMAGES, SUPPORTED_EXTENTIONS

import logging
import magic
import os

logger = logging.getLogger(__name__)


def image_is_valide(image: File = None):
    """check the image content_type agains the SUPPORTED_IMAGES config"""
    if image.content_type not in SUPPORTED_IMAGES:
        return False
    return True


def format_is_valid(ext: str = ''):
    """check the image extention agains the SUPPORTED_EXTENTIONS config"""
    if ext.lower() not in SUPPORTED_EXTENTIONS:
        return False
    return True


def get_content_type_by_file(filePath: str = ''):
    """return the MIME Type from a file given it's path"""
    mime = magic.Magic(mime=True)
    try:
        mime_type = mime.from_file(filePath)
        return mime_type
    except Exception as e:
        logger.error(e)
        raise e


def get_content_type_by_ext(ext: str = ''):
    """return the MIME Type of an extention"""
    supported_files_dict = dict(zip(SUPPORTED_EXTENTIONS, SUPPORTED_IMAGES))
    return supported_files_dict[ext]


def delete_file(filePath=None):
    """ Deletes a file from the filesystem given it's path"""
    try:
        os.remove(filePath)
    except Exception as e:
        logger.error(e)
        raise e
