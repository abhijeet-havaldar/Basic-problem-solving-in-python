#Q:Write a Python program that checks whether every even index contains an even number and every odd index contains an odd number of a given list.

def odd_even_position(nums):
    return all(nums[i] % 2 == i % 2 for i in range(len(nums)))


nums = [2,1,4,3,6,7,6,3]
print("Original list of numbers:",nums)
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))

nums = [2, 1, 4, 3, 6, 7, 6, 4]
print("Original list of numbers:",nums)
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))

nums = [4,1,2]
print("Original list of numbers:",nums)
print("Check whether every even index contains an even number and every \nodd index contains odd number of a given list:")
print(odd_even_position(nums))