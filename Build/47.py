#Q:Write a Python program that reads text (only alphabetical characters and spaces) and prints two words. The first word is the one that appears most often in the text. The second one is the word with the most letters

import collections

print("Input a text in a line.")

text_list = list(map(str, input().split()))

sc = collections.Counter(text_list)

commaon_word = sc.most_common()[0][0]

max_char =""

for s in text_list:
    if len(max_char) < len(s):
        max_char = s

print("\n Most frequent text and the word which has the maximum number of letters.")
print(commaon_word, max_char)