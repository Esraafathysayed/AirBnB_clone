#!/usr/bin/env python3
"""
command interpreter all common attributes/methods for other classesgi
"""

import cmd
from models.base_model import BaseModel
import models.engine

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand cls na
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quisfdat"""
        exit()

    def do_EOF(self, line):
        """Ex2e"""
        print()
        exit()
        
    def emptyline(self):
        """empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
