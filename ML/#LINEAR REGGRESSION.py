#LINEAR REGGRESSION
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Let's read the CSV file and package it into a DataFrame:
df = pd.read_csv('insurance.csv')

#Once the data is loaded in, let's take a quick peek at the first 5 values using the head() method:
print(df.head())

#We can also check the shape of our dataset via the shape property:
print("df.shape:         " , df.shape)

print("df.describe().round(2).T:\n",df.describe().round(2).T)

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Dataset Load karna
df = pd.read_csv("insurance.csv")

# Features (misal ke taur par 'age' aur 'bmi') aur Target ('charges')
X = df[["age", "bmi"]]
y = df["charges"]

# 2. Train-Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Regression Model (Random Forest Regressor)
reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_train_scaled, y_train)

# Predictions aur Evaluation
y_pred = reg.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
print(f"Regression R2 Score: {r2:.4f}")

# 5. Regression Graph Banana aur Save Karna
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color="teal", alpha=0.6)
plt.xlabel("Actual Insurance Charges")
plt.ylabel("Predicted Insurance Charges")
plt.title("Insurance Charges Regression: Actual vs Predicted")

# Perfect Fit Line (45-degree line)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linestyle="--",
    lw=2,
)

plt.tight_layout()
plt.savefig("insurance_regression_graph.png", dpi=300)
plt.close()

print("Regression graph successfully saved as 'insurance_regression_graph.png'!")