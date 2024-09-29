#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage  # Import the global storage instance

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            # If kwargs are provided, set attributes from the dictionary
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            # Default initialization (new instance)
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add the new instance to storage

    def save(self):
        """Updates the 'updated_at' timestamp and saves the instance to storage."""
        self.updated_at = datetime.now()
        storage.save()  # Save the updated object to storage

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
