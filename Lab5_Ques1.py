# Generate two tuples to represent two distinct points in space.
# (Three dimensional geometry). Determine the Euclidean distance between the two.

# ------------------------------CODE------------------------------------------

import math

point1 = tuple(map(float, input("Enter coordinates of the first point (x1, y1, z1) separated by spaces: ").split()))
point2 = tuple(map(float, input("Enter coordinates of the second point (x2, y2, z2) separated by spaces: ").split()))

distance = math.sqrt((point2[0] - point1[0]) ** 2 +
                     (point2[1] - point1[1]) ** 2 +
                     (point2[2] - point1[2]) ** 2)

print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")
