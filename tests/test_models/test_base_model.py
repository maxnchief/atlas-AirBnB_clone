import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_id_is_uuid(self):
        """Test that id is a valid UUID."""
        self.assertIsInstance(self.model.id, str)
        try:
            uuid_obj = uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save method updates updated_at."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict method returns a dictionary with correct keys."""
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_values(self):
        """Test that to_dict method returns correct values."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], self.model.__class__.__name__)

    def test_str_method(self):
        """Test the __str__ method."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)

if __name__ == '__main__':
    unittest.main()