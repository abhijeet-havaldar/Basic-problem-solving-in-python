#Q:Write a Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.


import struct

print(struct.calcsize("P") * 8)