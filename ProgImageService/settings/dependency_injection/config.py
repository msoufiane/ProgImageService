from repository.types.image_repository import ImageRepo
from repository.adapters.orm_adapter import ORMAdapter

import inject

def di_configuration(binder): 
    binder.bind(ImageRepo, ORMAdapter())