"""
The purpose of this signal is to delete the physical file from disk when deleting an Image record (from DB)
"""

from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_delete

from repository.utils import delete_file
from repository.models import Image

import logging

logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Image)
def delete_imageFile(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` signal"""
    try:
        delete_file(instance.file.path)
    except FileNotFoundError as e:
        logger.error('The file trying to delete is not found, file={}'.format(instance.file.path))
        raise e
