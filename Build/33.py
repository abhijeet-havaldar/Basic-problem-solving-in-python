#Q:Write a Python program to compute the digit number of the sum of two given integers.

print("Input two integers(a,b):")

a, b = map(int, input().split(" "))

print("Number of digits of a and b:")

print(len(str(a + b)))