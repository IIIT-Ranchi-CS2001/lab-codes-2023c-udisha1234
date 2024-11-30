# Define a function my_zip() that can form a list of tuples by iterating the following customer details:- 
# ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: 
# If strct = True, zipping shall be done only if all lists are of equal length. 
# If strct = False, zipping can be done by taking the minimum length of the iterable.


# --------------------------------------CODE-------------------------------------

def my_zip(*iterables, strct=True):

    if strct:
        lengths = [len(it) for it in iterables]
        if len(set(lengths)) > 1:
            raise ValueError("All lists must have the same length when 'strct=True'.")
    return list(zip(*iterables))


customer_name = ["Alice", "Bob", "Charlie"]
customer_id = [101, 102, 103]
shopping_points = [50, 75, 100]

try:
    print(my_zip(customer_name, customer_id, shopping_points, strct=True))
except ValueError as e:
    print(e)

print(my_zip(customer_name, customer_id, shopping_points[:2], strct=False))
