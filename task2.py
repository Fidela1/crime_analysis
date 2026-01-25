import pandas as pd

# Load dataset
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")

# 1. Identify unique provinces
unique_provinces = df["Province"].unique()
print("Unique Provinces:")
print(unique_provinces)
print("Total number of provinces:", len(unique_provinces))

# 2. Count total number of police stations
total_stations = df["Station"].nunique()
print("\nTotal number of police stations:", total_stations)

# 3. Count crime categories
crime_categories = df["Category"].nunique()
print("\nTotal number of crime categories:", crime_categories)
