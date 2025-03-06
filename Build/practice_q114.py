#Q:Write a Python program to filter positive numbers from a list

nums = [34,1,0,-23,12,-88]

print("Original numbers in the list:",nums)

new_list = list(filter(lambda x: x > 0, nums))
print("Positive numbers in the said list:",new_list)
