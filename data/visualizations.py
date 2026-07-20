import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("ds_salaries_cleaned.csv")

# Set a nice visual style
sns.set_style("whitegrid")

# Chart 1: Average salary by experience level
plt.figure(figsize=(8, 5))
order = df.groupby("experience_level")[
    "salary_in_usd"].mean().sort_values(ascending=False).index
sns.barplot(data=df, x="experience_level", y="salary_in_usd",
            order=order, hue="experience_level", legend=False, palette="viridis")
plt.title("Average Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.savefig("chart1_salary_by_experience.png")
plt.show()

# Chart 2: Salary trend over the years
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="work_year", y="salary_in_usd",
             errorbar=None, marker="o")
plt.title("Average Salary Trend Over the Years")
plt.xlabel("Year")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.savefig("chart2_salary_trend.png")
plt.show()

# Chart 3: Salary distribution (boxplot) by company size
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="company_size", y="salary_in_usd",
            hue="company_size", legend=False, palette="Set2")
plt.title("Salary Distribution by Company Size")
plt.xlabel("Company Size")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.savefig("chart3_salary_by_company_size.png")
plt.show()

print("All charts saved successfully as PNG files in the data folder!")
