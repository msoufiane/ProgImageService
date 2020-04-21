"""
Django settings for test environment for ProgImageService project.
"""

from .base import *

ALLOWED_HOSTS = ['localhost']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}