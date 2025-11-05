#Q:Write a Python program to check whether a given number is odd or even.
'''A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.'''

def oddish_evenish_num(n):
    return 'Oddish' if sum(map(int, str(n))) % 2 else 'Ecenish'


n = 120
print("Original Number:", n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(120))

n = 321
print("\nOriginal Number:", n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(321))

n = 43 
print("\nOriginal Number:", n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(43))

n = 4433
print("\nOriginal Number:", n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(4433))

n = 373
print("\nOriginal Number:", n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(373))