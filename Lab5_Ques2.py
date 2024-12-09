# Enter the coordinates of two points on the cartesian plane (take user input using comprehension). 
# Find the equation of the straight line passing through these points.

# ------------------------------CODE-------------------------------------------

point1 = [float(x) for x in input("Enter coordinates of the first point (x1, y1) separated by a space: ").split()]
point2 = [float(x) for x in input("Enter coordinates of the second point (x2, y2) separated by a space: ").split()]

x1, y1 = point1
x2, y2 = point2

if x1 == x2:
    print(f"The line is vertical and the equation is: x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)
    
    c = y1 - m * x1
    
    print(f"The equation of the line is: y = {m:.2f}x + {c:.2f}")
