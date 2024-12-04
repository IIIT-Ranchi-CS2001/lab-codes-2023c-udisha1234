# let's start ...

import pandas  as pd
import numpy as np

# Loading the data...
file_path = 'PythonLabData.csv'
Given_File_Data = pd.read_csv(file_path)

# Writing an interactive code ...

print("\n\n-------------------------------\"START\"---------------------------------------------\n\n")

# Ans 1 . Display the first 8 rows ...
x = input ("Want to see the first 8 rows of data ? ")
print(Given_File_Data.head(8))

# Ans 2. Display the last 5 rows ...
y = input ("Want to see the last 5 rows of data ? ")
print("\n\n-------------------------------\"NEXT\"---------------------------------------------\n\n")
print(Given_File_Data.tail(5))


# Ans 3. Show the dtype and numbers of non null values 
z = input ("Want to see the info of the data ? ")
print("\n\n-------------------------------\"NEXT\"---------------------------------------------\n\n")
print(Given_File_Data.info())


# Ans 4. Compute the mean AQI , max PM 2.5 and min PM 10 values for each city ...
a = input ("Continue ? ")
print("\n\n-------------------------------\"NEXT\"---------------------------------------------\n\n")
# Group by city and compute further
result = Given_File_Data.groupby('City').agg(
    Mean_AQI=('AQI', np.mean),
    Max_PM2_5=('PM2.5', np.max),
    Min_PM10=('PM10', np.min)
)
# Display the result
print(result)


# Convert the results to a dictionary
b = input("Want to see this in dictionary format ? ")
print("\n\n-------------------------------\"NEXT\"---------------------------------------------\n\n")
result_dict = result.apply(lambda row: [row['Mean_AQI'], row['Max_PM2_5'], row['Min_PM10']], axis=1).to_dict()

# Display the dictionary
print(result_dict)
