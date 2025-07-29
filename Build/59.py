#Q:A convex polygon is a simple polygon in which no line segment between two points on the boundary ever goes outside the polygon. Equivalently, it is a simple polygon whose interior is a convex set. In a convex polygon, all interior angles are less than or equal to 180 degrees, while in a strictly convex polygon all interior angles are strictly less than 180 degrees

def poly_area(c):
    add = []
    
    for i in range(0, (len(c) - 2), 2):
        add.append(c[i] * c[i + 3] - c[i + 1] * c[i + 2])
    
    add.append(c[len(c) - 2] * c[1] - c[len(c) - 1] * c[0])
    
    return abs(sum(add) / 2)

no_sides = int(input('Input number of sides: '))
cord_data = []

for z in range(no_sides):
    print("Side:", z+1)
    print("Input the Coordinate:")
    x = int(input('Input Coordinate x:'))
    y = int(input('Input Coordinate y:'))
    cord_data.append(x)
    cord_data.append(y)

print("\nArea of the Polygon:", poly_area(cord_data))
