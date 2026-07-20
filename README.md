# 📊 Engineering Job & Salary Trends Analysis Dashboard

A data analysis and machine learning project exploring salary trends in the data science job market, built as a 3rd semester engineering project.

## 🎯 Project Overview
This project analyzes a real-world dataset of data science job salaries to uncover trends across experience levels, job titles, remote work arrangements, and company sizes. It also includes a machine learning model to predict salaries and an interactive Streamlit dashboard for exploring the data.

## 📁 Dataset
**Data Science Job Salaries** by Ruchi Bhatia (Kaggle)
- 565 cleaned records (after removing duplicates)
- Columns: work_year, experience_level, employment_type, job_title, salary_in_usd, employee_residence, remote_ratio, company_location, company_size

## 🔍 Key Findings
- Salaries increase significantly with experience level: Entry ($61.6K) → Mid ($87.8K) → Senior ($138.4K) → Executive ($199.4K)
- Salaries have trended upward from 2020 to 2022
- Fully remote employees earn more on average ($120.8K) than hybrid workers ($80.7K)
- Company location and job title are the strongest predictors of salary — more influential than years of experience

## 🛠️ Tech Stack
- **Python** — core language
- **Pandas** — data cleaning and analysis
- **Matplotlib & Seaborn** — data visualization
- **Scikit-learn** — machine learning (Linear Regression & Random Forest)
- **Streamlit** — interactive web dashboard

## 📈 Machine Learning
Two models were built to predict salary:
| Model | R² Score | Mean Absolute Error |
|---|---|---|
| Linear Regression | 0.299 | $37,626 |
| Random Forest | 0.319 | $33,480 |

## 🚀 How to Run
1. Clone this repository
2. Install dependencies:.
pip install -r data/requirements.txt
3. Run the dashboard:
python -m streamlit run data/app.py
## 📂 Project Structure
career-trends-dashboard-/
├── data/
│   ├── ds_salaries.csv              # Raw dataset
│   ├── ds_salaries_cleaned.csv      # Cleaned dataset
│   ├── explore.py                   # Initial data exploration
│   ├── data_cleaning.py             # Data cleaning script
│   ├── eda.py                       # Exploratory data analysis
│   ├── visualizations.py            # Chart generation
│   ├── ml_prediction.py             # ML models
│   ├── app.py                       # Streamlit dashboard
│   └── requirements.txt             # Dependencies
└── README.md
## 👤 Author
Abhinanda Udupa — 3rd Semester Engineering Student
