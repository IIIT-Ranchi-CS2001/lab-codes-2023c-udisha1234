# Write a program to find:
# The equivalent impedance when two impedances Z1 and Z2 are connected in parallel. 
# Display Z1 and Z2 in complex form. 
# Display the real part and imaginary part of the result in separate lines.



# ---------------CODE-------------------------

def parallel_impedance(Z1, Z2):
    Z_eq = (Z1 * Z2) / (Z1 + Z2) 
    return Z_eq

Z1_real = float(input("Enter the real part of Z1: "))
Z1_imag = float(input("Enter the imaginary part of Z1: "))
Z2_real = float(input("Enter the real part of Z2: "))
Z2_imag = float(input("Enter the imaginary part of Z2: "))

Z1 = complex(Z1_real, Z1_imag)
Z2 = complex(Z2_real, Z2_imag)

print(f"\nZ1 in complex form: {Z1}")
print(f"Z2 in complex form: {Z2}")

Z_eq = parallel_impedance(Z1, Z2)

print(f"\nEquivalent Impedance (Z_eq): {Z_eq}")
print(f"Real part of Z_eq: {Z_eq.real}")
print(f"Imaginary part of Z_eq: {Z_eq.imag}")
