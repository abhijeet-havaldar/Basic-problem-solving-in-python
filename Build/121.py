#Q:Write a Python program to create a coded string from a given string, using a specified formula.

def test(input_str):
    translated_str = input_str.translate(str.maketrans('PTSHA','90168'))
    return translated_str

str1 = "PHP"
print("Original string:", str1)
print("Coded string: ", test(str1))

str2 = "JAVASCRIPT"
print("\nOriginal string: ", str2)
print("Coded string: ", test(str2))
