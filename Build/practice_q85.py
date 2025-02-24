#Q:Write a Python program to check whether a file path is a file or a directory.

import os

path = "abc.text"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file(socket,fifo,device file)")
print()