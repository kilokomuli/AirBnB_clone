#!/usr/bin/python3
""" contains the entry point of the command interpreter:
    must use module cmd
    class definition must be:class HBNBCommand(cmd.Cmd):
    comand interpretor shoul implement  Quit and EOF
    help and custom (hbnb)
    """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import models


class HBNBCommand(cmd.Cmd):
    """ class cmd"""
    prompt = "(hbnb) "
    classes_list = ["BaseModel"]
    commands_list = ["create", "show", "all", "destroy", "update", "count"]

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
        args = arg.split()
        if not self.class_verification(args):
            return

        inst = eval(str(args[0]) + '()')
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        class name and id """
        args = arg.split()

        if not self.class_verification(args):
            return

        if not self.id_verification(args):
            return

        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_key])

    def class_verification(self, args):
        """Verifies class and checks if it is in the class list.

        Returns:
            bool: True or false depending on status of class.
        """
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in self.classes_list:
            print("** class doesn't exist **")
            return False

        return True

    def id_verification(self, args):
        """Verifies id of class.

        Returns:
            bool: True or False depending on status of id.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False

        return True

    def do_all(self, arg):
        """Prints all string represntetion of all instances based
        or not on the class name"""
        args = arg.split()
        all_objects = models.storage.all()
        list_ = []
        if len(args) == 0:
            # print all classes
            for value in all_objects.values():
                list_.append(str(value))
        elif args[0] in self.classes_list:
            # print just arg[0] class instances
            for (key, value) in all_objects.items():
                if args[0] in key:
                    list_.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(list_)

    def do_update(self, arg):
        """Updates an istance based on the class name and id"""
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    models.storage.save()
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
