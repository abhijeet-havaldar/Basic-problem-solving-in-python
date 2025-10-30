#Q:Write a Python program to check whether a given sequence is linear, quadratic or cubic.

def Seq_Linear_Quadratic_Cubic(seq_nums):
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    
    if len(set(seq_nums)) == 1:
        return "Linear Sequence"
    
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    
    if len(set(seq_nums)) == 1:
        return "Quadratic Sequence"
    
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    
    if len(set(seq_nums)) == 1:
        return "Cubic Sequence"


nums = [0,2,4,6,8,10]
print("Original Sequence:", nums)
print("Check the said sequence is Linear, Quadratic, or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))

nums = [1,4,9,16,25]
print("\nOriginal Sequence:", nums)
print("Check the said sequence is Linear, Quadratic, or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))

nums = [0,12,10,0,-12,-20]
print("\nOriginal Sequence:", nums)
print("Check the said sequence is Linear, Quadratic, or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))

nums = [1,2,3,4,5]
print("\nOriginal Sequence:", nums)
print("Check the said sequence is Linear, Quadratic, or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
