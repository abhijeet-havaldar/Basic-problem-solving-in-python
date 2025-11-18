#Q:Write a Python program to compute the digit distance between two integers.
#The digit distance between two numbers is the absolute value of the difference of those numbers.

def digit_distance_nums(num1: int, num2: int) -> int:
    return sum(abs(i - j) for i,j in zip(map(int, str(num1)), map(int, str(num2))))

print(digit_distance_nums(509, 510))
print(digit_distance_nums(123, 256))
print(digit_distance_nums(23,56))
print(digit_distance_nums(1,2))
print(digit_distance_nums(24232, 45645))
