# WAP to count the number of each character present in a string using the concept of a dictionary.

# -----------------------------CODE------------------------------------------

input_string = input("Enter a string: ")

char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1  

print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
