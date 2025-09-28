#Q:Write a Python program to find the central character(s) of a given string. Return the two middle characters if the length of the string is even. Return the middle character if the length of the string is odd.

def middle_char(txt):
    return txt[(len(txt)-1)//2:(len(txt)+2)//2]

text = "Python"
print("Original string: ",text)
print("Middle character(s) of the said string: ",middle_char(text))

text = "PHP"
print("\nOriginal string: ",text)
print("Middle character(s) of the said string: ", middle_char(text))

text = "Java"
print("\nOriginal string: ",text)
print("Middle character(s) of the said string: ", middle_char(text))