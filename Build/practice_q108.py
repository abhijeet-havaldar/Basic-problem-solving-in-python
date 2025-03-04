#Q:Write a Python program to find the path to a file or directory when you encounter a path name.

import os 

for file in [__file__ ,os.path.dirname(__file__),'/','./broken_link']:
    print('file  :',file)
    print('Absolute :', os.path.isabs(file))
    print('Is file? :',os.path.isfile(file))
    print('Is Dir? :',os.path.isdir(file))
    print('Is link? :',os.path.islink(file))
    print('Exists? :',os.path.exists(file))
    print('link exists? :',os.path.lexists(file))