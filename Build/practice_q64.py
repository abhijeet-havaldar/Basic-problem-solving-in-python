#Q:Write a Python program that retrieves the date and time of file creation and modification.

import os.path, time

print("Last modified:%s"% time.ctime(os.path.getmtime("test.txt")))

print("created :%s"% time.ctime(os.path.getmtime("test.txt")))