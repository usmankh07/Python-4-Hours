class Greeter:
    def _init_(self, name):
        self.name = name
    def say_hello(self):
        print('Hello {}!'.format(self.name))
    def say_goodbye(self):
        print('goodbye {}!'.format(self.name))
# End of the class

my_greeter = Greeter()

print('get id, type and available methods and attributes for Greeter class.')
print(id(my_greeter))
print(type(my_greeter))
print(dir(my_greeter))
