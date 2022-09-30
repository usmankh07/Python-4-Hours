import inspect
import os
testvar = "Hello"
class Greeter:
    def _init_(self, name):
        self.name = name
    def say_hello(self):
        print("Hello {}!".format(self.name))
    def say_goodbye(self):
        print("Hello {}!".format(self.name))

    # End of class

my_greeter = Greeter()

#lambda function
exp = lambda x:x*x

# normal python user-definedfunction/method

def show_name_age(first_name:str, last_name:str, age:int):
    print("{} {} is {} years old".format(first_name, last_name, age))

inspect.getmembers(my_greeter) # returns members of the class

#introspection of ismodule
print('\n Checking if os is a module:', inspect.ismodule(os))
print('\n Checking if testvar is a module:', inspect.ismodule(testvar))
print('\n Inspect ismethod vs. isfunction comparison'.upper())

#introspection of isMethod
print('\n Ismethod:\n show_name_age:', inspect.ismethod(show_name_age),
    '\nexp:', inspect.ismethod(exp),
    '\nGreeter.say_hello:',
    inspect.ismethod(my_greeter.say_hello))

#introspection of isFunction

print('\n Isfunction:\n show_name_age:',
inspect.isfunction(show_name_age),
    '\nexp:', inspect.isfunction(exp),
    '\nGreeter.say_hello:', inspect.isfunction(my_greeter.say_hello))
