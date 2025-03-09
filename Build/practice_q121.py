#Q:Write a Python program to determine if a variable is defined or not.

try:
    x = 1 
except NameError:
    print("variable is not defined....!")
else:
    print("variable is defined.")

try:
    y
except NameError:
    print("variable is not defined...!")
else:
    print("variable is defined.")