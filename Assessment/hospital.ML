import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from itertools import combinations
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score

sns.set_style("whitegrid")


# 1) DATA LOAD & CLEANING (pandas + numpy)

df = pd.read_csv("Hospitals.csv")

 
df.replace(["NOT AVAILABLE", "NOT APPLICABLE", "-999", -999], np.nan, inplace=True)

# Numeric columns jo meaningful hain (ID/OBJECTID jaisay columns skip kiye)
numeric_cols = ["X", "Y", "POPULATION", "LATITUDE", "LONGITUDE", "TTL_STAFF", "BEDS"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Dataset shape:", df.shape)
print("\nNumeric columns summary:\n", df[numeric_cols].describe())


# 2)  NUMERIC COLUMN PAIR REGRESSION / CLASSIFICATION

R2_THRESHOLD = 0.10   # is se kam R2 = regression "theek se nahi ho rahi"
results = []

os_dir = "plots"
import os
os.makedirs(os_dir, exist_ok=True)

pair_num = 0
for col_x, col_y in combinations(numeric_cols, 2):
    pair_num += 1
    sub = df[[col_x, col_y]].dropna()
    if len(sub) < 30:
        continue

    X = sub[[col_x]].values
    y = sub[col_y].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---- REGRESSION ATTEMPT ----
    lin_model = LinearRegression()
    lin_model.fit(X_train, y_train)
    y_pred = lin_model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(6, 4))

    if r2 >= R2_THRESHOLD:
        # Regression  ->  No need classification 
        method = "REGRESSION"
        score_label = f"R2 = {r2:.3f}"
        sns.regplot(x=col_x, y=col_y, data=sub, ax=ax,
                    scatter_kws={"alpha": 0.4, "s": 12}, line_kws={"color": "red"})
        ax.set_title(f"{col_x} vs {col_y}  (Linear Regression)\n{score_label}")
        results.append({
            "col_x": col_x, "col_y": col_y, "method": method,
            "score_type": "R2", "score": round(r2, 3), "n": len(sub)
        })
    else:
        # Regression weak -> CLASSIFICATION try
        # target 2 classes (median split -> High / Low)
        median_val = sub[col_y].median()
        sub = sub.copy()
        sub["class_label"] = (sub[col_y] > median_val).astype(int)  # 1 = High, 0 = Low

        Xc = sub[[col_x]].values
        yc = sub["class_label"].values
        Xc_train, Xc_test, yc_train, yc_test = train_test_split(
            Xc, yc, test_size=0.2, random_state=42, stratify=yc
        )
        clf = LogisticRegression()
        clf.fit(Xc_train, yc_train)
        yc_pred = clf.predict(Xc_test)
        acc = accuracy_score(yc_test, yc_pred)

        method = "CLASSIFICATION"
        score_label = f"Accuracy = {acc:.3f}"
        sns.scatterplot(x=col_x, y=col_y, hue=sub["class_label"], data=sub,
                         palette={0: "steelblue", 1: "orangered"}, alpha=0.5, s=15, ax=ax)
        ax.set_title(f"{col_x} vs {col_y}  (Regression R2={r2:.3f} weak -> Classification)\n{score_label}")
        results.append({
            "col_x": col_x, "col_y": col_y, "method": method,
            "score_type": "Accuracy", "score": round(acc, 3), "n": len(sub),
            "regression_r2": round(r2, 3)
        })

    fname = f"{os_dir}/pair_{pair_num}_{col_x}_vs_{col_y}.png"
    plt.tight_layout()
    plt.savefig(fname, dpi=110)
    plt.close(fig)

# ---------------------------------------------------------
# 3) RESULTS SUMMARY
# ---------------------------------------------------------
results_df = pd.DataFrame(results)
results_df = results_df.sort_values("score", ascending=False)
results_df.to_csv("results_summary.csv", index=False)

print("\n\n================ FINAL SUMMARY ================\n")
print(results_df.to_string(index=False))

# Overall correlation heatmap (numpy + seaborn)
plt.figure(figsize=(7, 6))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap - Numeric Columns")
plt.tight_layout()
plt.savefig("plots/correlation_heatmap.png", dpi=110)
plt.close()

print("\nAll plots saved in 'plots/' folder. Summary saved as 'results_summary.csv'.")