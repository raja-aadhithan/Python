class MyClass:
    def __init__(self, name):
        self.name = name
        self.pretty_print_name()

    def pretty_print_name(self):
        print("This object's name is {}.".format(self.name))

my_objects = {}

name = 'obj_{}'.format(2)
my_objects[name] = my_objects.get(name, MyClass(name))
print(my_objects)