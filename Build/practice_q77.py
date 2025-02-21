#Q:Write a Python program to test whether the system is a big-endian platform or a little-endian platform.

import sys

print()

if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian platform.")

print()