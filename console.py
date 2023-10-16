import cmd
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at EOF.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or User, save it, and print its id.
        """
        args = arg.split()
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args or len(args) < 2:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        args = arg.split()
        if not args or len(args) < 2:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all string representations of instances based on the class name.
        """
        args = arg.split()
        objects = storage.all()
        if not args or len(args) == 0:
            print([str(obj) for obj in objects.values()])
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if args[0] in str(obj)])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id with a specific attribute and value.
        """
        args = arg.split()
        if not args or len(args) < 4:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        attr_name = args[3]
        try:
            attr_value = eval(args[4])
        except (NameError, SyntaxError):
            attr_value = args[4]
        setattr(objects[key], attr_name, attr_value)
        storage.save()

        def do_tests(self, arg):
            """Run all unit tests interactively and uniinteractively"""
            unittest.main(argv=[''], exit=False)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

