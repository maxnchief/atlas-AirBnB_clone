#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"