#SIMPLECASE insurance
import numpy as np
import pandas as pd

# Step 1: CSV sahi tarike se load karo
df = pd.read_csv("insurance.csv")
print(df.head())
print(df.info())

# Step 2: Saare categorical (text) columns ko encode karo
df = pd.get_dummies(df, columns=["sex", "smoker"], drop_first=True)

# Step 3: Ab features (X) aur target (y) nikalo
X = df.drop("region", axis=1).copy()   # region ke ilawa sab features
y = df["region"].copy()                 # jo predict karna hai

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Step 4: Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, train_size=0.7, random_state=25
)

# Step 6: Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 7: Predict & Evaluate
preds = model.predict(X_test)
print(classification_report(y_test, preds))