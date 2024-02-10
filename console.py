#!/usr/bin/python3
""" contains the entry point of the command interpreter:
    must use module cmd
    class definition must be:class HBNBCommand(cmd.Cmd):
    comand interpretor shoul implement  Quit and EOF
    help and custom (hbnb)
    """
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to
        JSON file and prints the id"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string represntetion of all instances based
        or not on the class name"""
        args = arg.split()
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Updates an istance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
