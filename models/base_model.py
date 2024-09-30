#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        if kwargs:
            # Re-create an instance from the dictionary (kwargs)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert string to datetime object
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Create a new instance
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the `updated_at` attribute and saves the object."""
        self.updated_at = datetime.now()
        from models import storage  # Lazy loading to avoid circular import
        storage.save()  # Call the save method on the storage

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        # Convert datetime objects to ISO format strings
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
