import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error

# Load the cleaned dataset
df = pd.read_csv("ds_salaries_cleaned.csv")

# 1. Select features (now including job_title and employee_residence)
features = ["experience_level", "employment_type", "job_title",
            "remote_ratio", "company_size", "company_location", "work_year"]
target = "salary_in_usd"

X = df[features].copy()
y = df[target]

# 2. Convert text columns into numbers
label_encoders = {}
for col in ["experience_level", "employment_type", "job_title", "company_size", "company_location"]:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# 3. Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ---- MODEL 1: Linear Regression (baseline) ----
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_r2 = r2_score(y_test, lr_pred)
lr_mae = mean_absolute_error(y_test, lr_pred)

# ---- MODEL 2: Random Forest (more powerful) ----
rf_model = RandomForestRegressor(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)

# ---- Compare both models ----
print("===== Model Comparison =====")
print(f"Linear Regression   -> R²: {lr_r2:.3f} | MAE: ${lr_mae:,.2f}")
print(f"Random Forest        -> R²: {rf_r2:.3f} | MAE: ${rf_mae:,.2f}")

# ---- Feature importance (Random Forest tells us what matters most) ----
importance = pd.Series(rf_model.feature_importances_,
                       index=features).sort_values(ascending=False)
print("\nWhich features matter most for predicting salary:")
print(importance)

# ---- Sample predictions using the better model ----
print("\nSample predictions (Random Forest) vs actual:")
comparison = pd.DataFrame(
    {"Actual": y_test.values[:10], "Predicted": rf_pred[:10].round(2)})
print(comparison)
