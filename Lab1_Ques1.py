# Write a program to find the:
# Sum,  
# Difference,   
# Product,  
# Integer quotient,
# Remainder 
# Fractional quotient
# of two numbers. Enter the numbers on run time. Display the input data and results in neat format


# -------------------------------------------------------------------------
# ----------------------------CODE-----------------------------------------
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the results
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Check for division by zero
if num2 != 0:
    int_quotient = int(num1 // num2)  # Integer quotient
    remainder = num1 % num2
    fractional_quotient = num1 / num2
else:
    int_quotient = "Undefined (division by zero)"
    remainder = "Undefined (division by zero)"
    fractional_quotient = "Undefined (division by zero)"

# Display results in a neat format
print("\nResults:")
print(f"First Number: {num1}")
print(f"Second Number: {num2}")
print("-" * 30)
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Integer Quotient: {int_quotient}")
print(f"Remainder: {remainder}")
print(f"Fractional Quotient: {fractional_quotient}")
