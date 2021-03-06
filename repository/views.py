from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

from repository.usecases.image_usecase import ImageUseCase, ImageNotFoundError
from repository.utils import image_is_valide, get_content_type_by_file, get_content_type_by_ext, format_is_valid

import logging

logger = logging.getLogger(__name__)
uc = ImageUseCase()


@api_view(['POST'])
def save_image_view(request):
    if (not request.data) or (not request.FILES):
        return Response('Field `image` is missing in the request body', status=status.HTTP_400_BAD_REQUEST)

    imageFile = None
    try:
        imageFile = request.FILES['image']
    except KeyError:
        return Response('Field `image` is missing in the request body', status=status.HTTP_400_BAD_REQUEST)

    if not image_is_valide(imageFile):
        return Response('Unsupported file format', status=status.HTTP_400_BAD_REQUEST)

    imageID = uc.save_image(imageFile)

    if not imageID:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"id": imageID}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def retrieve_image_view(request, id):
    image = None
    try:
        image = uc.retrieve_image(id)
    except ImageNotFoundError:
        logger.warn('Couldn\'t find an image with the provided id. id={}'.format(id))
        return Response(status=status.HTTP_404_NOT_FOUND)
    return HttpResponse(image.file, content_type=get_content_type_by_file(image.file.path))


@api_view(['GET'])
def convert_image_view(request, id, ext):
    logger.debug('Converting image id={} to {}'.format(id, ext))
    converted_image = None

    if not format_is_valid(ext):
        return Response('Unsupported file extention ({})'.format(ext), status=status.HTTP_400_BAD_REQUEST)

    try:
        original_image = uc.retrieve_image(id)
        converted_image = uc.convert_image(original_image.file, ext)

        if not converted_image:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return HttpResponse(converted_image, content_type=get_content_type_by_ext(ext))
    except ImageNotFoundError:
        logger.warn('Couldn\'t find an image with the provided id. id={}'.format(id))
        return Response(status=status.HTTP_404_NOT_FOUND)
