#Q:Write a Python program that accepts a list of numbers. Count the negative numbers and compute the sum of the positive numbers of the said list. Return these values through a list

def count_sum(nums):
    if not nums:
        return []
    
    return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]

nums = [1, 2, 3, 4, 5]
print("Original list:", nums)
print("Number of negative numbers and sum of positive numbers:", count_sum(nums))

nums = [-1, -2, -3, -4, -5]
print("Original list:", nums)
print("Number of negative numbers and sum of positive numbers:", count_sum(nums))

nums = [1, 2, 3, -4, -5]
print("Original list:", nums)
print("Number of negative numbers and sum of positive numbers:", count_sum(nums))

nums = [1, 2, -3, -4, -5]
print("Original list:", nums)
print("Number of negative numbers and sum of positive numbers:", count_sum(nums))
