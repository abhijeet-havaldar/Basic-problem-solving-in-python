#Q:Write a Python program to check if two given numbers are Co Prime or not. Return True if two numbers are Co Prime otherwise return false.

def gcd(p,q):
    while q != 0:
        p,q = q,p % q
    return p

def is_coprime(x,y):
    return gcd(x,y) == 1

print(is_coprime(17, 13))
print(is_coprime(17,21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))