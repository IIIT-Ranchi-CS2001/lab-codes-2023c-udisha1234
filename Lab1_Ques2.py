# Write python program to find
# (a) Area and perimeter of a triangle when all three sides are given. Hint: (Use Heron’s Equation)
# (b) Find all three angles of the triangle given in (a)
# Display the input data and results in proper format.


# ----------------CODE-----------------------------

import math

side_a = float(input("Enter the first side of the triangle (a): "))
side_b = float(input("Enter the second side of the triangle (b): "))
side_c = float(input("Enter the third side of the triangle (c): "))

perimeter = side_a + side_b + side_c
semi_perimeter = perimeter / 2

area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * 
                 (semi_perimeter - side_b) * (semi_perimeter - side_c))

angle_A = math.degrees(math.acos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)))
angle_B = math.degrees(math.acos((side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)))
angle_C = math.degrees(math.acos((side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)))

print("\nResults:")
print(f"Sides of the Triangle: a = {side_a}, b = {side_b}, c = {side_c}")
print("-" * 40)
print(f"Perimeter of the Triangle: {perimeter:.2f}")
print(f"Area of the Triangle: {area:.2f}")
print("-" * 40)
print(f"Angles of the Triangle (in degrees):")
print(f"Angle A: {angle_A:.2f}°")
print(f"Angle B: {angle_B:.2f}°")
print(f"Angle C: {angle_C:.2f}°")
