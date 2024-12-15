import pandas as pd
import numpy as np

# Step 1: Create data using NumPy
data = {
    "ID": np.arange(1, 11),  # Create an array of IDs from 1 to 10
    "Name": [f"User{i}" for i in range(1, 11)],  # Generate usernames like User1, User2, ...
    "Age": np.random.randint(20, 40, size=10),  # Generate random ages between 20 and 40
    "Score": np.random.uniform(50, 100, size=10).round(2),  # Generate random scores between 50.0 and 100.0
    "Is_Active": np.random.choice([True, False], size=10)  # Randomly assign True/False
}

# Step 2: Create a Pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Display the DataFrame
print("Generated DataFrame:")
print(df)

# Step 4: Save to a CSV file
df.to_csv("sample_dataframe.csv", index=False)  # Save as CSV file
print("\nDataFrame saved to 'sample_dataframe.csv'")
