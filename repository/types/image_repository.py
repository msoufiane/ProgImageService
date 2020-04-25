"""
The Image repository interface
"""

from abc import ABCMeta, abstractmethod
from django.core.files import File

class ImageRepo(metaclass=ABCMeta):
    @abstractmethod
    def saveImage(self, imageFile:File):
        pass

    @abstractmethod
    def retrieveImage(self, id):
        pass