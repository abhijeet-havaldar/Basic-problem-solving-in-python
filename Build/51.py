#Q:Write a Python program that determines the difference between the largest and smallest integers created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 


print("Input an integer created by 8 numbers from 0 to 9.:")

num = list(input())

print("Difference between the largest and the smallest integer from the given integer:")

print(int("".join(sorted(num, reverse=True))) - int("".join(sorted(num))))