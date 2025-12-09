#Q:Write a Python program to convert the letters of a given string (same case-upper/lower) into alphabetical order.

def test(input_str):
    return ''.join(sorted(input_str))


str1 = "PHP"
print("Original string:", str1)
print("Convert the letters of the said string into alphabetical order:", test(str1))

str2 = "javascript"
print("\nOriginal string:", str2)
print("Convert the letters of the said string into alphabetical order:", test(str2))

str3 = "python"
print("\nOriginal string:", str3)
print("Convert the letters of the said string into alphabetical order:", test(str3))