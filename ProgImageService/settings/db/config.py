"""
Config file for the default database to be used, override this in environment config file if needed
"""

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            '..',
            'db.sqlite3'),
    }
}