import pandas as pd

# Load the dataset
df = pd.read_csv("ds_salaries.csv")

# Show the first 5 rows
print(df.head())

# Show basic info: column names, data types, missing values
print(df.info())
