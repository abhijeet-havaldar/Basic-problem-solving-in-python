#Q:Write a Python program to reverse all words of odd lengths# Define a function named reverse_even that reverses the even-length words in a given text.
def reverse_even(txt):
    reversed_words = [i[::-1] if not len(i) % 2 else i for i in txt.split()]

    return ' '.join(reversed_words)


print(reverse_even("The quick brown fox jumps over the lazy dog"))

print(reverse_even("Python Exercises"))
