#!/usr/bin/python3
import cmd
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new User"""
        user = User()
        user.first_name = input("First Name: ")
        user.last_name = input("Last Name: ")
        user.email = input("Email: ")
        user.password = input("Password: ")
        user.save()
        print(user.id)

    def do_show(self, arg):
        """Shows a User by ID"""
        args = arg.split()
        if len(args) < 1:
            print("** user id missing **")
            return
        user = storage.all().get(f"User.{args[0]}")
        if user:
            print(user)
        else:
            print("** no user found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
    try:
        args = arg.split()
        if len(args) != 2:
            print("Usage: destroy <User> <id>")
        cls = globals().get(args[0])
        if not cls:
            print(f"Class '{args[0]}' not found")
        obj = cls.get(args[1])
        obj.delete()
        print(f"{cls.__name__} with id {obj.id} deleted")

    except Exception as e:
        print(f"Error: {e}")

    def do_update(self, arg):
        """Updates a User's attributes"""
        args = arg.split()
        if len(args) < 4:
            print("** insufficient arguments **")
            return
        user_key = f"User.{args[0]}"
        user = storage.all().get(user_key)
        if user:
            setattr(user, args[1], args[2])
            user.save()
        else:
            print("** no user found **")

    def do_all(self, arg):
        """Shows all Users"""
        users = [str(user) for user in storage.all().values() if isinstance(user, User)]
        print(users)
