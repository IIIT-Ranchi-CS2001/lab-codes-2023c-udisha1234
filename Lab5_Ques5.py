# Sort the list of tuples constructed above with and without sorted function. 

# --------------------------------CODE---------------------------------------

customer_names = ["Alice", "Bob", "Charlie"]
customer_ids = [101, 102, 103]
shopping_points = [200, 150, 300]

list_of_tuples = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]

sorted_with_sorted = sorted(list_of_tuples, key=lambda x: x[1])

sorted_without_sorted = list_of_tuples[:]
for i in range(len(sorted_without_sorted)):
    for j in range(len(sorted_without_sorted) - i - 1):
        if sorted_without_sorted[j][1] > sorted_without_sorted[j + 1][1]:
            sorted_without_sorted[j], sorted_without_sorted[j + 1] = sorted_without_sorted[j + 1], sorted_without_sorted[j]

print("Original list of tuples:")
print(list_of_tuples)

print("\nList of tuples sorted by Customer ID (using sorted):")
print(sorted_with_sorted)

print("\nList of tuples sorted by Customer ID (without using sorted):")
print(sorted_without_sorted)
