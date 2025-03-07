#Q:Write a Python program to compute the product of a list of integers (without using a for loop).

from functools import reduce

nums = [10,20,30]

print("original list numbers:")
print(nums)

nums_product = reduce((lambda x,y:x*y),nums)

print("\nproduct of the said numbers(without using a for loop):",nums_product)

print("\nproduct of the said number (without using a for loop):",nums_product)