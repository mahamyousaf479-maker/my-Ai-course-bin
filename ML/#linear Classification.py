#linear Classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Dataset Load 
df = pd.read_csv('AB_NYC_2019.csv')

# Missing valuesa
df_clean = df.dropna(subset=['reviews_per_month']).copy()
le = LabelEncoder()
df_clean['room_type_encoded'] = le.fit_transform(df_clean['room_type'])


num_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns.tolist()


print("==================================================")
print("PAIR-WISE NUMERICAL COLUMNS CLASSIFICATION RESULTS")
print("==================================================")

pairs = [(num_cols[i], num_cols[i+1]) for i in range(len(num_cols)-1)]

for col1, col2 in pairs:
    
    X = df_clean[[col1, col2]]
    y = df_clean['room_type_encoded']
    
    # Train-Test Split 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Classification Model (Random Forest Classifier)
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train_scaled, y_train)
    
    # Prediction aur Accuracy check karna
    y_pred = clf.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Features Used: [{col1}, {col2}] ==> Classification Accuracy: {acc * 100:.2f}%")

print("==================================================")
print("Classification successfully completed on all numerical column pairs!")




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Dataset Load karna
df = pd.read_csv('AB_NYC_2019.csv')

# Missing values handle karna
df_clean = df.dropna(subset=['reviews_per_month']).copy()

# Target variable (Price) ke ilawa baaki numerical columns ki list nikalna
num_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns.tolist()
if 'price' in num_cols:
    num_cols.remove('price')

# 2. Pehlay do numerical columns uthana, phir aglay do, pairs ki shakal mein regression lagana
print("==================================================")
print("PAIR-WISE NUMERICAL COLUMNS REGRESSION RESULTS")
print("==================================================")

pairs = [(num_cols[i], num_cols[i+1]) for i in range(len(num_cols)-1)]

for col1, col2 in pairs:
    # Features (X) mein 2 numerical columns aur Target (y) mein 'price'
    X = df_clean[[col1, col2]]
    y = df_clean['price']
    
    # Train-Test Split (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Regression Model (Random Forest Regressor)
    reg = RandomForestRegressor(n_estimators=50, random_state=42)
    reg.fit(X_train_scaled, y_train)
    
    # Prediction aur R2 Score check karna
    y_pred = reg.predict(X_test_scaled)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Features: [{col1}, {col2}] ==> R2 Score: {r2:.4f}")

print("==================================================")
print("Regression successfully completed on all numerical column pairs!")

df_clean = df.dropna(subset=["reviews_per_month"]).copy()
import matplotlib.pyplot as plt
# Features (misal ke taur par minimum_nights aur number_of_reviews) aur Target ('price')
X = df_clean[["minimum_nights", "number_of_reviews"]]
y = df_clean["price"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Regressor Model
reg = RandomForestRegressor(n_estimators=50, random_state=42)
reg.fit(X_train_scaled, y_train)
y_pred = reg.predict(X_test_scaled)

# 2. Graph Banana (Actual vs Predicted Price)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color="purple", alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Regression: Actual vs Predicted Price")

# Perfect Prediction Line (45-degree line)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linestyle="--",
    lw=2,
)

plt.tight_layout()
plt.savefig("regression_graph.png", dpi=300)  # Graph save ho jaye ga
plt.close()