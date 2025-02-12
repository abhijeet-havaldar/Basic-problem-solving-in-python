#Q:Write a Python program to list all files in a directory

from os import listdir
from os.path import isfile,join

files_list = [f for f in listdir ('/home/student') if isfile (join('/home/student',f))]


print(files_list)
