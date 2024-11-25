# Write a python script to enter any string at run time and check whether it is a palindrome or not.

# ---------------------CODE----------------------------------

input_string = input("Enter a string: ")

normalized_string = input_string.replace(" ", "").lower()

if normalized_string == normalized_string[::-1]:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
