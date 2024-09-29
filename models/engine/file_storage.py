import json
from models.user import User  # Make sure to import User class
from models.base_model import BaseModel

class FileStorage:
    # ... existing methods

    def all(self):
        """Returns a dictionary of all stored objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Loads the objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "User":
                        obj = User(**value)
                    else:
                        obj = BaseModel(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
