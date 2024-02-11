#!/usr/bin/env python3
"""
The console the entry point to
command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand cls na
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quisfdat"""
        exit()

    def do_EOF(self, line):
        """Exit22e"""
        print()
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
