#!/usr/bin/python3
'''this is the console module'''


import cmd
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_help(self, arg):
        return super().do_help(arg)
    
    def do_EOF(self,line):
        print("")
        return True
    
    def do_quit(self, arg):
        return True
    
    def emptyline(self) -> bool:
        return super().emptyline()

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
        """Destroys a User by ID"""
        args = arg.split()
        if len(args) < 1:
            print("** user id missing **")
            return
        user_key = f"User.{args[0]}"
        if user_key in storage.all():
            del storage.all()[user_key]
            storage.save()
        else:
            print("** no user found **")

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
