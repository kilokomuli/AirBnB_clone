#!/usr/bin/python3
""" contains the entry point of the command interpreter:
    must use module cmd
    class definition must be:class HBNBCommand(cmd.Cmd):
    comand interpretor shoul implement  Quit and EOF
    help and custom (hbnb)
    """
import cmd


class HBNBCommand(cmd.Cmd):
    """ class cmd"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the progrma using EOF ctr+d"""
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
