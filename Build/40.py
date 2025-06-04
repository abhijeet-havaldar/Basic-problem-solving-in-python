#Q:Write a Python program to check if a point (x,y) is in a triangle or not. A triangle is formed by three points.

print("Enter 8 numbers (x1 y1 x2 y2 x3 y3 xp yp):")
inputs = input().split()

if len(inputs) != 8:
    print(" Error: You must enter exactly 8 numbers.")
else:
    x1, y1, x2, y2, x3, y3, xp, yp = map(float, inputs)

    def cross_product(xa, ya, xb, yb, xp, yp):
        return (xb - xa) * (yp - ya) - (yb - ya) * (xp - xa)

    c1 = cross_product(x1, y1, x2, y2, xp, yp)
    c2 = cross_product(x2, y2, x3, y3, xp, yp)
    c3 = cross_product(x3, y3, x1, y1, xp, yp)

    if (c1 >= 0 and c2 >= 0 and c3 >= 0) or (c1 <= 0 and c2 <= 0 and c3 <= 0):
        print("The point is in the triangle.")
    else:
        print("The point is outside the triangle.")

