#Q:Write a Python program to test if a variable is a list, tuple, or set.

x = ('tuple',False, 3.2,1)

if type(x) is list:
    print("x is a list")
elif type(x) is set:
    print("x is a set")
elif type(x) is tuple:
    print("x is a tuple")
else:
    print("Neither a list nor a set nor a tuple.")