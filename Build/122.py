#Q:Write a Python program to check if a given string contains only lowercase or uppercase characters.

def test(input_str):
    return input_str.islower() or input_str.isupper()

str1 = "PHP"
print("Original string: ", str1)
print("Coded string: ", test(str1))

str2 = "javascript"
print("Original string: ",str2)
print("Coded string: ", test(str2))

str3 = "JavaScript"
print("Original string: ", str3)
print("Coded string: ", test(str3))