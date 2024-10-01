import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        pass

    def test_create_missing_class_name(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_class_name(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_instance_id(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        """Test show command with no instance found"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_missing_class_name(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class_name(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_instance_id(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """Test destroy command with no instance found"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all_invalid_class_name(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_class_name(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class_name(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_instance_id(self):
        """Test update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_no_instance_found(self):
        """Test update command with no instance found"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing value"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234 name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

if __name__ == '__main__':
    unittest.main()