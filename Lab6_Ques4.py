# Write a python script using map, lambda and filter functions to do the following operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22 2@$” 
# To find all the letters given in the string and to convert them to uppercase
# o/p: [‘TOM’]
# To find all the digits present in the string and to find their squares
# o/p: [625]
# To display all the alphanumeric characters present in the string
# o/p: [“Tom”, ‘25’, “Rahu22”]


# -----------------------------------CODE------------------------------------

input_string = input("Enter a comma-separated string: ").split(',')

letters_to_upper = list(
    map(lambda x: x.upper(), filter(lambda x: x.isalpha(), input_string))
)

digits_squares = list(
    map(lambda x: int(x) ** 2, filter(lambda x: x.isdigit(), input_string))
)

alphanumerics = list(filter(lambda x: x.isalnum(), input_string))

print("Uppercase letters:", letters_to_upper)
print("Squares of digits:", digits_squares)
print("Alphanumeric characters:", alphanumerics)
