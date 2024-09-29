#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage  # Import storage to handle persistence

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the `updated_at` attribute and saves the object."""
        self.updated_at = datetime.now()
        storage.save()  # Call the save method on the storage

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
