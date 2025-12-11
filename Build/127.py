#Q:Write a Python program to check whether the average value of the elements of a given array of numbers is a whole number or not.

import array as arr

def test(nums):
    return sum(nums) % len(nums) == 0

array_num = arr.array('i',[1,3,5,7,9])

print("Original array: ")
for i in range(len(array_num)):
    print(array_num[i], end=' ')

print("\nCheck the average value of the elements of the said array is whole number or not: \n", test(array_num))

array_num = arr.array('i',[2,4,2,6,4,8])

print("\nOriginal array:")
for i in range(len(array_num)):
    print(array_num[i], end=" ")

print("\nCheck the average value of the element of the said array is a whole number  or not:\n ", test(array_num))