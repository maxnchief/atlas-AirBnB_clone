import unittest
from models.amenity import Amenity

#!/usr/bin/python3
'''Unit tests for the Amenity class'''



class TestAmenity(unittest.TestCase):
    '''Test cases for the Amenity class'''

    def setUp(self):
        '''Set up for the tests'''
        self.amenity = Amenity()

    def test_instance(self):
        '''Test if the object is an instance of Amenity'''
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attribute(self):
        '''Test the name attribute'''
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_name_set(self):
        '''Test setting the name attribute'''
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict(self):
        '''Test to_dict method'''
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_str(self):
        '''Test the __str__ method'''
        string = str(self.amenity)
        self.assertIn('[Amenity]', string)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)


if __name__ == '__main__':
    unittest.main()