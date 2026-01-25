import pandas as pd

# Load dataset
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")

# Select the year for analysis
year = "2015-2016"

# Group by province and sum crimes for the selected year
province_crimes = df.groupby("Province")[year].sum()

print("Total crimes per province in", year)
print(province_crimes)

# Identify province with highest and lowest crime
highest_province = province_crimes.idxmax()
lowest_province = province_crimes.idxmin()

print("\nProvince with highest crime:", highest_province,
      "with", province_crimes.max(), "crimes")

print("Province with lowest crime:", lowest_province,
      "with", province_crimes.min(), "crimes")
