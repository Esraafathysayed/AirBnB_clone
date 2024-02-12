#!/usr/bin/env python3
"""
The console the entry point to
command interpreter
"""

import cmd
import sys
from models.__init__ import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = '(hbnb) '

    Base_clas = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """Quit command"""
        exit()

    def do_EOF(self, line):
        """Exit the program"""
        print()
        exit()

    def emptyline(self):
        """empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        lines = line.split(' ')

        if not lines or not lines[0]:
            print("** class name missing **")
            return

        if lines[0] not in self.Base_clas.keys():
            print("** class doesn't exist **")
            return

        get_class = self.Base_clas[lines[0]]
        var_class = get_class()
        var_class.save()
        print(var_class.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id"""
        args = line.split(' ')

        if not args or not args[0]:
            print("** class name missing **")
            return

        if args[0] not in self.Base_clas.keys():
            print("** class doesn't exist **")
            return

        if not args or len(args) < 2 or not args[1]:
            print("** instance id missing **")
            return

        base_key = args[0] + '.' + args[1]

        all_objects = storage.all()

        if base_key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects.get(base_key))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args_des = line.split(' ')

        if not args_des or not args_des[0]:
            print("** class name missing **")
            return

        if args_des[0] not in self.Base_clas.keys():
            print("** class doesn't exist **")
            return

        if not args_des or len(args_des) < 2 or not args_des[1]:
            print("** instance id missing **")
            return

        args_key = args_des[0] + '.' + args_des[1]

        if args_key not in storage.all():
            print("** no instance found **")
            return

        del (storage.all()[args_key])
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name"""
        args_all = line.split(' ')

        to_show = []

        if not args_all or not args_all[0]:
            for value in storage.all().values():
                to_show.append(str(value))
        elif args_all[0]:
            if args_all[0] not in self.valid_classes.keys():
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if key.split('.')[0] == args_all[0]:
                    to_show.append(str(value))

        print(to_show)

    def do_update(self, line):
        """Update class attributes"""
        args_update = line.split(' ')

        if not args_update or not args_update[0]:
            print("** class name missing **")
            return

        if args_update[0] not in self.Base_clas.keys():
            print("** class doesn't exist **")
            return

        if not args_update or len(args_update) < 2 or not args_update[1]:
            print("** instance id missing **")
            return

        dic_key = args_update[0] + '.' + args_update[1]

        if dic_key not in storage.all():
            print("** no instance found **")
            return

        if not args_update or len(args_update) < 3 or not args_update[2]:
            print("** attribute name missing **")
            return

        if not args_update or len(args_update) < 4 or not args_update[3]:
            print("** value missing **")
            return

        setattr(storage.all()[dic_key], args_update[2], args_update[3].strip('"'))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
