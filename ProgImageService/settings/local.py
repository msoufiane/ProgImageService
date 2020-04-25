"""
ProgImageService settings for local environment, override any defaults here.
"""

from ProgImageService.settings.base import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'DEFINE_A_SECURE_KEY')
ALLOWED_HOSTS = ['localhost']
DEBUG = True

