# PANDAS & File operations:

# And perform the following tasks:
# Check if the file `election_data.csv` exists in the directory. If not, create the file and write the election data into it. Handle file-related exceptions gracefully.
# Read the data into a Pandas DataFrame and calculate the percentage of seats won by each party. Add this as a new column named Seats_Percentage.
# Determine the party with the highest number of seats in each state and display their names.
# Create a bar chart showing the number of seats won by each party in each state using Matplotlib or Seaborn.
# Ensure your script includes exception handling for file reading, writing, and any potential calculation errors.


# -----------------------------------CODE------------------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "State": ["Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh", "Madhya Pradesh",
              "Rajasthan", "Rajasthan", "Rajasthan", "Rajasthan"],
    "Party": ["BJP", "INC", "BSP", "Others", "BJP", "INC", "BSP", "Others"],
    "Seats_Won": [163, 66, 0, 1, 115, 69, 2, 13],
    "Total_Seats": [230, 230, 230, 230, 200, 200, 200, 200],
    "Voter_Turnout (%)": [72.1, 72.1, 72.1, 72.1, 74.2, 74.2, 74.2, 74.2]
}

filename = "election_data.csv"

try:
    if not os.path.exists(filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"{filename} created successfully.")
    else:
        print(f"{filename} already exists.")

    df = pd.read_csv(filename)

    df["Seats_Percentage"] = (df["Seats_Won"] / df["Total_Seats"]) * 100

    highest_seat_parties = df.loc[df.groupby("State")["Seats_Won"].idxmax()]
    print("\nParty with the highest number of seats in each state:")
    print(highest_seat_parties[["State", "Party", "Seats_Won"]])

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="State", y="Seats_Won", hue="Party")
    plt.title("Seats Won by Each Party in Each State")
    plt.xlabel("State")
    plt.ylabel("Seats Won")
    plt.legend(title="Party")
    plt.tight_layout()

    plt.show()

except FileNotFoundError:
    print("Error: The file was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
