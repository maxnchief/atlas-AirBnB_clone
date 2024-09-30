import json
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    def __init__(self):
        """Initialize FileStorage with a file path and an empty objects dictionary."""
        self.__file_path = "file.json"  # Set your desired file path here
        self.__objects = {}  # Initialize an empty dictionary to store objects

    def all(self):
        """Returns a dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Loads the objects from the JSON file."""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name in self.class_mapping:
                        obj = self.class_mapping[class_name](**value)
                        self.new(obj)
        except FileNotFoundError:
            # No file to load from, so do nothing
            pass
