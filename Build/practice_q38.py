#Q:Write a Python program to solve (x + y) * (x + y).

x,y = 4,3

result  = x * x + 2 * x * y + y * y

print("({} + {}) ^2) = {}".format(x,y,result))