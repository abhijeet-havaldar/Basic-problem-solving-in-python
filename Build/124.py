#Q:Write a Python program to check if a given string contains two similar consecutive letters.

def test(input_str):
    return any(c1 == c2 for c1, c2 in zip(input_str, input_str[1:]))

str1 = "PHP"
print("Original string: ", str1)
print("Check for consecutive similar letters!", test(str1))

str2 = "PHHP"
print("Original string: ",str2)
print("Check for consecutive similar letters!", test(str2))

str3 = "PHPP"
print("\nOriginal string: ",str3)
print("Check for consecutive similar letters!", test(str3))