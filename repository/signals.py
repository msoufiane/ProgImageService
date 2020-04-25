from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_delete

from repository.models import Image
from repository.utils.delete_file import delete_file


@receiver(post_delete, sender=Image)
def delete_imageFile(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    try:
        delete_file(instance.file.path)
    except FileNotFoundError as e:
        raise e