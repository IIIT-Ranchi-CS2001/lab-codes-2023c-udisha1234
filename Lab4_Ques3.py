# Generate 2 lists (course code and course name). 
# create a new list with both course code and name like["CS1001:Python",...]

# ------------------------------CODE----------------------------------

course_codes = input("Enter course codes separated by spaces: ").split()

course_names = input("Enter course names separated by commas: ").split(',')

if len(course_codes) != len(course_names):
    print("Error: The number of course codes and names must match.")
else:
    courses = [f"{code}:{name.strip()}" for code, name in zip(course_codes, course_names)]
    
    print("Combined Course List:")
    print(courses)
