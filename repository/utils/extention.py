from django.core.files.base import File
from repository.settings import SUPPORTED_IMAGES
import magic
import logging

logger = logging.getLogger(__name__)

def is_valide(file:File=None):
    if not file.content_type in SUPPORTED_IMAGES:
        return False
    return True

def content_type(filePath:str):
    mime = magic.Magic(mime=True)
    return mime.from_file(filePath)