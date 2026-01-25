import pandas as pd

# Load the dataset
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")

# Select the crime category
crime_category = "All theft not mentioned elsewhere"
filtered_df = df[df["Category"] == crime_category]

# Select only year columns
year_columns = [
    '2005-2006', '2006-2007', '2007-2008', '2008-2009',
    '2009-2010', '2010-2011', '2011-2012', '2012-2013',
    '2013-2014', '2014-2015', '2015-2016'
]

# Calculate total crimes per year
total_crimes_per_year = filtered_df[year_columns].sum()

print("Total crimes per year for:", crime_category)
print(total_crimes_per_year)

# Identify highest and lowest crime years
highest_year = total_crimes_per_year.idxmax()
lowest_year = total_crimes_per_year.idxmin()

print("\nYear with highest crime:", highest_year,
      "with", total_crimes_per_year.max(), "crimes")

print("Year with lowest crime:", lowest_year,
      "with", total_crimes_per_year.min(), "crimes")
