import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Career Trends Dashboard", layout="wide")

# Load data
df = pd.read_csv("ds_salaries_cleaned.csv")

# Title
st.title("📊 Data Science Job & Salary Trends Dashboard")
st.write("Explore salary trends across experience levels, job titles, remote work, and company size.")

# Sidebar filters
st.sidebar.header("Filters")
selected_exp = st.sidebar.multiselect(
    "Experience Level",
    options=df["experience_level"].unique(),
    default=df["experience_level"].unique()
)

selected_size = st.sidebar.multiselect(
    "Company Size",
    options=df["company_size"].unique(),
    default=df["company_size"].unique()
)

# Filter the data based on sidebar selections
filtered_df = df[
    (df["experience_level"].isin(selected_exp)) &
    (df["company_size"].isin(selected_size))
]

# Key stats
col1, col2, col3 = st.columns(3)
col1.metric("Average Salary", f"${filtered_df['salary_in_usd'].mean():,.0f}")
col2.metric("Median Salary", f"${filtered_df['salary_in_usd'].median():,.0f}")
col3.metric("Total Records", f"{len(filtered_df)}")

st.divider()

# Chart 1: Salary by experience level
st.subheader("Average Salary by Experience Level")
fig1, ax1 = plt.subplots(figsize=(8, 4))
order = filtered_df.groupby("experience_level")[
    "salary_in_usd"].mean().sort_values(ascending=False).index
sns.barplot(data=filtered_df, x="experience_level", y="salary_in_usd",
            order=order, hue="experience_level", legend=False, palette="viridis", ax=ax1)
ax1.set_xlabel("Experience Level")
ax1.set_ylabel("Salary (USD)")
st.pyplot(fig1)

# Chart 2: Salary trend over years
st.subheader("Salary Trend Over the Years")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.lineplot(data=filtered_df, x="work_year", y="salary_in_usd",
             errorbar=None, marker="o", ax=ax2)
ax2.set_xlabel("Year")
ax2.set_ylabel("Salary (USD)")
st.pyplot(fig2)

# Chart 3: Salary by company size
st.subheader("Salary Distribution by Company Size")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.boxplot(data=filtered_df, x="company_size", y="salary_in_usd",
            hue="company_size", legend=False, palette="Set2", ax=ax3)
ax3.set_xlabel("Company Size")
ax3.set_ylabel("Salary (USD)")
st.pyplot(fig3)

# Raw data table
st.subheader("Raw Data")
st.dataframe(filtered_df)
