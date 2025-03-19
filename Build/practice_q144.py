#Q:Write a Python program to check whether a variable is an integer or string.

def test(n):

    if type(n) == int:
        return "It is a integer"
    else:
        return "It is a string"
    
print(test(12))
print(test('23312'))