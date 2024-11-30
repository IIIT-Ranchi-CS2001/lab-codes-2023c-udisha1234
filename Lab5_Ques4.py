# Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. 
# Construct a list of tuples with and without using built-in function zip().

# --------------------------------CODE------------------------------------------

customer_names = [name.strip() for name in input("Enter customer names separated by commas: ").split(",")]
customer_ids = [int(id.strip()) for id in input("Enter customer IDs separated by commas: ").split(",")]
shopping_points = [int(points.strip()) for points in input("Enter shopping points separated by commas: ").split(",")]

list_of_tuples_zip = list(zip(customer_names, customer_ids, shopping_points))

list_of_tuples_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

print("\nList of tuples (using zip):")
print(list_of_tuples_zip)

print("\nList of tuples (without using zip):")
print(list_of_tuples_manual)
