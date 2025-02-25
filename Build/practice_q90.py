#Q:Write a Python program to create a copy of its own source code.

def file_copy(src,dest):
    with open(src) as f, open (dest,'w') as d:


     file_copy("untitled0.py","a.py")
with open('a.py','r') as filehandle:
    for line in filehandle:
        print(line,end='')