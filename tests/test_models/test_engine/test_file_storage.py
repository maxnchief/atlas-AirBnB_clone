import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test that new adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test that save properly saves objects to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("test_file.json", "r") as file:
            data = json.load(file)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], obj.id)

    def test_reload(self):
        """Test that reload properly loads objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)
    
    def test__file_path(self):
        """Test that the file path is set correctly"""
        self.assertEqual(self.storage._FileStorage__file_path, "test_file.json")

    def test_objects(self):
            """Test that objects are stored correctly in __objects"""
            obj1 = BaseModel()
            obj2 = User()
            self.storage.new(obj1)
            self.storage.new(obj2)
            key1 = f"BaseModel.{obj1.id}"
            key2 = f"User.{obj2.id}"
            self.assertIn(key1, self.storage.all())
            self.assertIn(key2, self.storage.all())
            self.assertEqual(self.storage.all()[key1], obj1)
            self.assertEqual(self.storage.all()[key2], obj2)


if __name__ == "__main__":
    unittest.main()