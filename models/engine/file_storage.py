import json
from models.user import User  # Make sure to import User class
from models.base_model import BaseModel

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
                    # Debugging print
                    print(f"Reloading object of class {class_name} with key {key}")
                    if class_name == "User":
                        obj = User(**value)
                    else:
                        obj = BaseModel(**value)
                    self.new(obj)
        except FileNotFoundError:
            print("File not found. No objects to load.")
            pass  # This is fine; it simply means there was nothing to load
