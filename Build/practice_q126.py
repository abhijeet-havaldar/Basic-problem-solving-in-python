#Q:Write a Python program to get the actual module object for a given object.

import inspect

def add(x,y):
    return x + y

print(inspect.getmodule(add))