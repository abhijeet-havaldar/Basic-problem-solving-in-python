#Q:Write a Python program to check whether lowercase letters exist in a string.

def lower_case_str(text):
    ctr = 0

    for char in text:
        if(ord(char) >= 97 and ord(char) <= 122):
            ctr = ctr + 1
    
    if(ctr > 0):
        return True

str1 = 'A8238i8acdeOUEI'
print("Original string :",str1)
print("Lowercase letter exist in said string :",lower_case_str(str1))

str1 = 'PYTHON'
print("\nOriginal string:",str1)
print("Lowercase letter exist in the said string :",lower_case_str(str1))

str1 = 'javascript'
print("\nOriginal string :",str1)
print("Lowercase letter exist in the said string :",lower_case_str(str1))