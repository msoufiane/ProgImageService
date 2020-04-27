"""
Logger configuration file
"""

import logging.config
import os
from django.utils.log import DEFAULT_LOGGING

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGLEVEL = os.environ.get('DJANGO_LOGLEVEL', 'debug').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [ %(levelname)-8s] [%(name)-12s] %(message)s',
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        'repository': {
            'level': LOGLEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
        'noisy_module': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    },
})
