#Q:Write a Python program to create the maximum number of regions obtained by drawing n given straight lines

while True:
    print("Input number of straight lines (0 to exit):")

    n = int(input())
    if n <= 0:
        break
    print("number of regions:")
    print((n*n + n + 2)//2)