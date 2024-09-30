import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def test_initialization(self):
        """Test that User is properly initialized"""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """Test the string representation of the User instance"""
        self.user.id = "1234"
        self.user.email = "test@example.com"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        expected_str = "[User] (1234) {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}"
        self.assertEqual(str(self.user), expected_str)

if __name__ == '__main__':
    unittest.main()