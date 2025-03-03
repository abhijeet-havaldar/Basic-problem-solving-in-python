#Q:Write a Python program to retrieve file properties.

import os.path
import time

print()
print('file     :',__file__)
print('Access time:',time.ctime(os.path.getatime(__file__)))
print('Modified time:',time.ctime(os.path.getmtime(__file__)))
print('Change time:',time.ctime(os.path.getctime(__file__)))
print('size  :',os.path.getsize(__file__))