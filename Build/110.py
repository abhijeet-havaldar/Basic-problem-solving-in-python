#:Write a Python program to remove duplicate numbers from a given list of numbers.

def unique_nums(nums):
    return [i for i in nums if nums.count(i) == 1]

nums = [1,2,3,2,3,4,5]
print("Original list of numbers:", nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))

nums = [1,2,3,2,4,5]
print("\nOriginal list of numbers:", nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))

nums = [1,2,3,4,5]
print("\nOriginal list of numbers:", nums)
print("After removing the duplicate numbers from the said list:")
print(unique_nums(nums))