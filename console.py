#!/usr/bin/python3
'''This is the console module.'''

import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
            return
        
        # Create instance and save
        instance = eval(arg)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(instance_key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        if instance_key in storage.all():
            del storage.all()[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg and arg not in ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
            return

        instances = []
        for key, instance in storage.all().items():
            if arg:
                if key.startswith(arg):
                    instances.append(str(instance))
            else:
                instances.append(str(instance))
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(instance_key)
        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        value = args[3].strip('"')  # Remove quotes if present
        
        # Cast value to the appropriate type
        if value.isdigit():
            value = int(value)
        try:
            value = float(value)
        except ValueError:
            pass  # Keep it as a string if conversion fails
        
        setattr(instance, attribute_name, value)
        instance.save()

    def do_EOF(self):
        """Exits the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Quits the program."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
