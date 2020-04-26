"""
The Image converter interface
"""

from abc import ABCMeta, abstractmethod
from django.core.files import File

class ImageConverter(metaclass=ABCMeta):
    @abstractmethod
    def convertImage(self, imageFile:File):
        pass
