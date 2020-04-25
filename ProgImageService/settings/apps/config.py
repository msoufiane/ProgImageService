"""
Config file for the installed apps to use by the service
"""

# Django modules
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

# 3rd party libraries
INSTALLED_APPS += [
    'rest_framework',
]

# Custom Apps
INSTALLED_APPS += [
    'repository',
]
