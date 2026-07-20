import pandas as pd

# Load the dataset
df = pd.read_csv("ds_salaries.csv")

# 1. Drop the useless "Unnamed: 0" column (just a leftover index)
df = df.drop(columns=["Unnamed: 0"])

# 2. Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# 3. Check for duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())

# 4. Standardize text columns to lowercase (avoids "Full-time" vs "full-time" mismatches)
df["employment_type"] = df["employment_type"].str.lower()
df["experience_level"] = df["experience_level"].str.lower()
df["company_size"] = df["company_size"].str.lower()

# 5. Save the cleaned data to a new file
# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Save the cleaned data to a new file
df.to_csv("ds_salaries_cleaned.csv", index=False)
print("\nCleaning done! Cleaned file saved as ds_salaries_cleaned.csv")
print(df.head())
print("Final shape after cleaning:", df.shape)
