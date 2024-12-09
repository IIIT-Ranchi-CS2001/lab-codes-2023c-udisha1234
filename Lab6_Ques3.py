# Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *

# -------------------------------CODE--------------------------------------

def my_max(*args):

    if not args:
        raise ValueError("No elements provided to find the maximum.")
    
    max_value = args[0]
    for item in args[1:]:
        if item > max_value:
            max_value = item
    
    return max_value



data_list = [3, 5, 2, 9, 7]
print("Max in list:", my_max(*data_list)) 

data_set = {4, 1, 8, 6}
print("Max in set:", my_max(*data_set)) 

data_tuple = (10, 20, 15, 5)
print("Max in tuple:", my_max(*data_tuple))  
