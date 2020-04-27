"""
ProgImageService settings for production environment, override any defaults here.
"""

from ProgImageService.settings.base import *
import os


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'DEFINE_A_SECURE_KEY')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']  # It shoud be the domaine name

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "progimage"),
        "USER": os.environ.get("SQL_USER", "progimage"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "progimage"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

DEBUG = False
