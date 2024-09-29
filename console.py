#!/usr/bin/python3
"""AirBnB Clone - Command Interpreter"""

import cmd
import sys
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB objects"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
