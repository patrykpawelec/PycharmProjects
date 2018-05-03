"""
This module contains Calculator class
"""
class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current
""" documentation string for module my_module
This module contains hello_world function
"""
def hello_world(name):
    print("Hello, World! My name is %s" % name)

"""
Modules in Python are simply Python files with the .py extension containing Python definitions and statements. 
Modules can be handy when you want to use your function in a number of programs without copying its definition into each program. 
Modules are imported from other modules using the import keyword and the file name without an extension. 
The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. 
Import the module my_module and use the hello_world function. 
"""
import calculator
calc = calculator.Calculator()    # create new instance of Calculator class defined in calculator module
calc.add(2)
print(calc.get_current())
import my_module
my_module.hello_world('Patryk')

import datetime
print(datetime.datetime.today())

from calculator import Calculator
calc = Calculator()    # here we can use Calculator class directly without prefix calculator.
calc.add(2)
print(calc.get_current())
from my_module import hello_world
print(hello_world())    # Note: hello_world function used without prefix

