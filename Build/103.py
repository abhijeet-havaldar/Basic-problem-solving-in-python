#Q:Write a Python program to check whether two given lines are parallel or not.

def parallel_lines(line1,line2):
    return line1[0]/line1[1] == line2[0]/line2[1]

print(parallel_lines([2,3,4], [2,3,8]))
print(parallel_lines([2,3,4], [4,-3,8]))
