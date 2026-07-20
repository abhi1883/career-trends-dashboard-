import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("ds_salaries_cleaned.csv")

# 1. Basic statistics on salary
print("Salary statistics (in USD):")
print(df["salary_in_usd"].describe())

# 2. Average salary by experience level
print("\nAverage salary by experience level:")
print(df.groupby("experience_level")[
      "salary_in_usd"].mean().sort_values(ascending=False))

# 3. Average salary by job title (top 10 highest paying)
print("\nTop 10 highest paying job titles:")
print(df.groupby("job_title")["salary_in_usd"].mean(
).sort_values(ascending=False).head(10))

# 4. Number of employees per experience level
print("\nNumber of employees per experience level:")
print(df["experience_level"].value_counts())

# 5. Average salary by remote ratio
print("\nAverage salary by remote work ratio:")
print(df.groupby("remote_ratio")["salary_in_usd"].mean())
