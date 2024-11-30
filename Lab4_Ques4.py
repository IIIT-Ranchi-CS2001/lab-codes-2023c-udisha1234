# Generate two sets – first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate the following sets 
# of all artists of the class
# allrounders of the class
# dancers but not singers
# singers but not dancers
# dancers but not singers cum singers but not dancers


# ---------------------------CODE----------------------------------


singers = {name.strip() for name in input("Enter names of all singers (separated by commas): ").split(",")}
dancers = {name.strip() for name in input("Enter names of all dancers (separated by commas): ").split(",")}

all_artists = singers | dancers  
allrounders = singers & dancers  
dancers_not_singers = dancers - singers  
singers_not_dancers = singers - dancers 
exclusive_artists = singers ^ dancers

print(f"All artists: {all_artists}")
print(f"Allrounders: {allrounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Dancers but not singers cum singers but not dancers: {exclusive_artists}")
