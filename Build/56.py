#Q:Write a Python program to sum all numerical values (positive integers) embedded in a sentence


import sys
import re

def test(stri):
    print("Input some text and numeric values ( to exit):")
    numeric_sum = sum(map(int, re.findall(r"[0-9]{1,5}", stri)))

    print("Sum of the numeric balues:", numeric_sum)

print(test("sd1fdsfs23 dssd56"))
print(test("15apple2banana"))
print(test("flowers5fruit5"))