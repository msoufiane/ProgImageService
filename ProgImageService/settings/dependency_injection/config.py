"""
Config file binding interfaces implementation to their usecases
change here if you need to use another implementation of the intended interfaces
"""

from repository.types.image_repository import ImageRepo
from repository.types.image_converter import ImageConverter

from repository.adapters.orm_adapter import ORMAdapter
from repository.adapters.pil_adapter import PILAdapter


import inject

def di_configuration(binder): 
    binder.bind(ImageConverter, PILAdapter())
    binder.bind(ImageRepo, ORMAdapter())
