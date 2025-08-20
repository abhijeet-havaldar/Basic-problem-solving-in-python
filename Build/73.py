#Q:Write a Python program that removes duplicate elements from a given array of numbers so that each element appears only once and returns the new length of the array.

def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]

    return len(nums)

print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
print(remove_duplicates([1,2,2,3,4,4]))