#Q:Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string

print("Input a text with two words 'Python' and 'Jawa'" )

text = input().split()

for i in range(len(text)):
    if "Python" in text[i]:
        n = text[i].index("Python")
        text[i] = text[i][:n] + "Jawa" + text[i][n + 6:]
    elif "Jawa" in text[i]:
        n = text[i].index("Jawa")
        text[i] = text[i][:n] + "Python" + text[i][n + 4:]
    
print(*text)