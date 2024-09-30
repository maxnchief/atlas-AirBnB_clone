import unittest
from models.review import Review
from models.base_model import BaseModel

#!/usr/bin/python3
'''Unit tests for the Review class'''



class TestReview(unittest.TestCase):
    '''Test cases for the Review class'''

    def setUp(self):
        '''Set up method for each test'''
        self.review = Review()

    def test_instance(self):
        '''Test if review is an instance of Review'''
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        '''Test if review has the correct attributes'''
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attributes_default(self):
        '''Test the default values of attributes'''
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        '''Test if Review inherits from BaseModel'''
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_to_dict(self):
        '''Test to_dict method'''
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_str(self):
        '''Test the __str__ method'''
        string = str(self.review)
        self.assertIn('[Review]', string)
        self.assertIn('id', string)
        self.assertIn('created_at', string)
        self.assertIn('updated_at', string)


if __name__ == '__main__':
    unittest.main()