"""
Image django model
"""

from django.db import models

class Image(models.Model):
    file = models.FileField(blank=False, null=False, upload_to='uploads/')
