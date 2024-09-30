import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        '''Set up for the tests'''
        self.city = City()

    def test_instance(self):
        '''Test if city is an instance of BaseModel'''
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        '''Test if city has the correct attributes'''
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_state_id_type(self):
        '''Test if state_id is a string'''
        self.assertIsInstance(self.city.state_id, str)

    def test_name_type(self):
        '''Test if name is a string'''
        self.assertIsInstance(self.city.name, str)

if __name__ == "__main__":
    unittest.main()