import pandas as pd

# Load dataset
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")

# Display first 5 rows
print(df.head())

# Rows and columns
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

# Column names
print("Columns:", df.columns.tolist())
