#Diamond.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Dataset Load karna
df = pd.read_csv("diamonds.csv")

print("==================================================")
print("1. REGRESSION MODEL (Predicting Diamond Price)")
print("==================================================")

# Regression: Hum 'carat' aur 'depth' se diamond ki 'price' predict karenge
X_reg = df[["carat", "depth"]]
y_reg = df["price"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

scaler_r = StandardScaler()
X_train_r_scaled = scaler_r.fit_transform(X_train_r)
X_test_r_scaled = scaler_r.transform(X_test_r)

reg = RandomForestRegressor(n_estimators=50, random_state=42)
reg.fit(X_train_r_scaled, y_train_r)
y_pred_r = reg.predict(X_test_r_scaled)

r2 = r2_score(y_test_r, y_pred_r)
print(f"Regression R2 Score: {r2:.4f}")


print("==================================================")
print("2. CLASSIFICATION MODEL (Predicting Diamond Cut)")
print("==================================================")

# Target variable ('cut') ko numbers mein convert karna
le = LabelEncoder()
df["cut_encoded"] = le.fit_transform(df["cut"])

# Classification: Hum 'carat' aur 'price' se diamond ka 'cut' predict karenge
X_clf = df[["carat", "price"]]
y_clf = df["cut_encoded"]

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)

scaler_c = StandardScaler()
X_train_c_scaled = scaler_c.fit_transform(X_train_c)
X_test_c_scaled = scaler_c.transform(X_test_c)

clf = RandomForestClassifier(n_estimators=50, random_state=42)
clf.fit(X_train_c_scaled, y_train_c)
y_pred_c = clf.predict(X_test_c_scaled)

accuracy = accuracy_score(y_test_c, y_pred_c)
print(f"Classification Accuracy: {accuracy * 100:.2f}%")
print("==================================================")