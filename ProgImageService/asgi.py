"""
ASGI config for ProgImageService project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProgImageService.settings.{0}'.format(ENVIRONMENT))

application = get_asgi_application()
