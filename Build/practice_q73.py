#Q:Write a Python program to calculate the midpoints of a line.

print('\n calculate the midpoint of a line.')

x1 = float(input('the value of x (the first endpoint)'))
y1 = float(input('the value of y (the first endpoint)'))

x2 =float(input('the value of x (the first endpoint)'))
y2 = float(input('the value of y(the first endpoint)'))

x_m_point = (x1 + x2) / 2

y_m_point =  (y1 + y2) / 2 

print("the midpoint of the line is:")
print("the midpoint's x value is:",x_m_point)
print("the midpoint's y value is:",y_m_point)