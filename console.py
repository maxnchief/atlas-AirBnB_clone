#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""

print("Starting the command interpreter...")

# Import the necessary modules
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Initialize file storage
storage = FileStorage()
storage.reload()

class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB clone objects"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program"""
        print()  # New line before exit
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
