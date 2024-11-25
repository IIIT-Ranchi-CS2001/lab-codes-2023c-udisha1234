# Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
# Hint: find the discriminant d= b2 − 4ac
# If d = 0, the equation has one real repeated root (both roots are the same: 
# R1= R2 = -b/(2a)

# If d > 0, the equation has two distinct real roots.
# 	R1= (-b + sqrt(d))/2a
# R2= (-b - sqrt(d))/2a
 
# If d < 0, the equation has two complex roots.
# real_part = -b / (2 * a) 
# imaginary_part = math.sqrt(-discriminant) / (2 * a)


# --------------------------CODE-----------------------------------------

import math


def find_roots(a, b, c):
    if a == 0:
        print("Coefficient 'a' cannot be 0 for a quadratic equation.")
        return

    discriminant = b**2 - 4*a*c
    print(f"Discriminant (d): {discriminant}")

    if discriminant > 0:
        R1 = (-b + math.sqrt(discriminant)) / (2 * a)
        R2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The equation has two distinct real roots: R1 = {R1}, R2 = {R2}")
    elif discriminant == 0:
        R1 = R2 = -b / (2 * a)
        print(f"The equation has one real repeated root: R1 = R2 = {R1}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print(f"The equation has two complex roots:")
        print(f"R1 = {real_part} + {imaginary_part}i")
        print(f"R2 = {real_part} - {imaginary_part}i")

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

find_roots(a, b, c)
