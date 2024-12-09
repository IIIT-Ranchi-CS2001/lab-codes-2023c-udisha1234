# For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
# The length of the string S
# The first occurrence of the letter ‘e’
# The total number of occurrences of ‘a’
# Generate “Ta Ta Black Sheep”


# ------------------------CODE---------------------------------

S = "Ba Ba Black Sheep"

length_of_string = len(S)
print(f"The length of the string S: {length_of_string}")

first_occurrence_e = S.find('e')
if first_occurrence_e != -1:
    print(f"The first occurrence of 'e': {first_occurrence_e}")
else:
    print("The letter 'e' does not exist in the string.")

# as there might be some case sensitive case ...
total_occurrences_a = S.lower().count('a') 
print(f"The total number of occurrences of 'a': {total_occurrences_a}")

new_string = S.replace("Ba", "Ta", 1)
print(f"Generated string: {new_string}")
