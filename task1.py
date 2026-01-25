import pandas as pd

# Load dataset
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")

# Display first 5 rows
print(df.head())

# Rows and columns
print("Shape:", df.shape)

# Column names
print("Columns:", df.columns.tolist())
