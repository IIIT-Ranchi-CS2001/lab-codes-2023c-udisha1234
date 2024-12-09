# If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# “mAHA bHARAT”
# “Bharat”
# “BharatBharatBharat”
# “Mera Bharat”
# “Mera Bharat Mahan”


# -----------------------CODE---------------------------------

S1 = "Maha Bharat"

# 1. "mAHA bHARAT"
string1 = S1.swapcase()
print(f"1. {string1}")

# 2. "Bharat"
string2 = S1.split()[1]
print(f"2. {string2}")

# 3. "BharatBharatBharat"
string3 = string2 * 3
print(f"3. {string3}")

# 4. "Mera Bharat"
string4 = "Mera " + string2
print(f"4. {string4}")

# 5. "Mera Bharat Mahan"
string5 = string4 + " Mahan"
print(f"5. {string5}")
