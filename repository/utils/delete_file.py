import os

def delete_file(path=None):
   """ Deletes a file from filesystem."""
   try:
       os.remove(path)
   except Exception as e:
       raise e