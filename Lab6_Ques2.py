# Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. 
# The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points

# ----------------------------CODE--------------------------------------

def my_sort(data, key=0):

    if not data or not isinstance(data, list) or not all(isinstance(i, tuple) for i in data):
        raise ValueError("Invalid data. Expected a list of tuples.")
    
    if key < 0 or key >= len(data[0]):
        raise ValueError("Key index out of range.")
    
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data


data = [
    ("Alice", 101, 50),
    ("Charlie", 103, 100),
    ("Bob", 102, 75)
]

sorted_by_name = my_sort(data[:], key=0)
print("Sorted by customer name:", sorted_by_name)

sorted_by_id = my_sort(data[:], key=1)
print("Sorted by customer ID:", sorted_by_id)

sorted_by_points = my_sort(data[:], key=2)
print("Sorted by shopping points:", sorted_by_points)
