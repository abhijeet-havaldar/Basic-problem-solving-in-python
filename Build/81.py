#Q:Write a Python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.

import random

print(random.sample([i for i in range(1,100) if i % 2 == 0],10))