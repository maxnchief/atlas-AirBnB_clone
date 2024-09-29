#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Initialize the storage engine
storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter to manage AirBnB objects"""

    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
        else:
            try:
                # Dynamically create an instance of the provided class
                new_instance = eval(args)()
                storage.new(new_instance)
                storage.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Shows the string representation of an instance based on class and id"""
        tokens = args.split()
        if len(tokens) < 2:
            print("** class name or id missing **")
        else:
            obj_key = f"{tokens[0]}.{tokens[1]}"
            obj = storage.all().get(obj_key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_quit(self, args):
        """Quits the command interpreter"""
        return True

    def do_EOF(self, args):
        """Handles EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
