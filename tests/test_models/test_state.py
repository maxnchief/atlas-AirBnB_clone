import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        '''Set up for the tests'''
        self.state = State()

    def test_state_instance(self):
        '''Test if state is an instance of BaseModel'''
        self.assertIsInstance(self.state, State)

    def test_state_attributes(self):
        '''Test if state has the attribute name and it's an empty string'''
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_state_name_assignment(self):
        '''Test assigning a name to the state'''
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

if __name__ == "__main__":
    unittest.main()