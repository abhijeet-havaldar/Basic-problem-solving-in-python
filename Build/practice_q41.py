#Q:Write a Python program to check whether a file exists.

import os.path

print(os.path.isfile('main.txt'))
print(os.path.isfile('a.py'))