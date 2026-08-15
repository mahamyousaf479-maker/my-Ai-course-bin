
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

sns.set_style("whitegrid")
PLOT_DIR = "plots_timeseries"
os.makedirs(PLOT_DIR, exist_ok=True)



# 1) LOAD & CLEAN DATA

def load_and_clean(path):
    """Load the raw CSV and separate hospital metadata from procedure price columns."""
    df = pd.read_csv(path)
    df = df.rename(columns={df.columns[0]: "hospital"})

    meta_cols = ["hospital", "address", "lat", "long"]
    price_cols = [c for c in df.columns if c not in meta_cols]

    # Prices should be numeric; coerce anything odd to NaN
    df[price_cols] = df[price_cols].apply(pd.to_numeric, errors="coerce")

    return df, meta_cols, price_cols


df, meta_cols, price_cols = load_and_clean("OR_hos_prices1.csv")

print("Shape:", df.shape)
print("Hospitals:", df.shape[0], "| Procedures (price columns):", len(price_cols))
print("Overall missing %% in price matrix: %.1f%%" %
      (df[price_cols].isna().mean().mean() * 100))


# =======================================================================================
# 2) EXPLORATORY DATA ANALYSIS (Pandas + NumPy + Seaborn)
# =======================================================================================

# --- 2a. Missingness heatmap: which hospitals/procedures are sparsely reported ---
plt.figure(figsize=(14, 8))
sns.heatmap(df[price_cols].isna(), cbar=False, cmap="mako")
plt.title("Missing Data Map (white = missing) — Hospitals x Procedures")
plt.xlabel("Procedure"); plt.ylabel("Hospital index")
plt.xticks([]); plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/01_missingness_heatmap.png", dpi=110)
plt.close()

# --- 2b. Median price per procedure -> this defines our sequence order ---
procedure_median = df[price_cols].median(numeric_only=True).sort_values()

plt.figure(figsize=(9, 14))
sns.barplot(x=procedure_median.values, y=procedure_median.index, color="teal")
plt.title("Procedures Ranked by Median Price\n(this ordering = our time-series axis)")
plt.xlabel("Median Price ($)")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/02_procedure_price_ranking.png", dpi=110)
plt.close()

# --- 2c. Correlation among the 20 most-reported (least-missing) procedures ---
most_reported = df[price_cols].notna().sum().sort_values(ascending=False).head(20).index
plt.figure(figsize=(11, 9))
sns.heatmap(df[most_reported].corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Between the 20 Most-Reported Procedures")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/03_correlation_heatmap.png", dpi=110)
plt.close()

print("EDA plots saved to", PLOT_DIR)


# =======================================================================================
# 3) BUILD THE "COST-ESCALATION" SEQUENCE PER HOSPITAL
# =======================================================================================
def build_hospital_sequences(df, price_cols, procedure_median):
    """
    Reorders each hospital's prices along the cheap->expensive procedure axis,
    then fills missing values via linear interpolation along that sequence
    (falling back to the procedure's overall median at the sequence edges).
    Each hospital's curve is then scaled to [0, 1] with its own MinMaxScaler
    so the model learns SHAPE (how costs escalate) rather than absolute size.
    Returns: sequences (n_hospitals, n_procedures), one scaler per hospital.
    """
    ordered_cols = procedure_median.index.tolist()
    ordered = df[ordered_cols].copy()

    sequences = []
    scalers = []
    for i in range(len(ordered)):
        row = ordered.iloc[i].astype(float)
        # interpolate along the ordered procedure axis (linear), then fill remaining
        # edge NaNs with the global procedure median (best available estimate)
        row_interp = row.interpolate(limit_direction="both")
        row_interp = row_interp.fillna(procedure_median[ordered_cols])

        scaler = MinMaxScaler()
        seq_scaled = scaler.fit_transform(row_interp.values.reshape(-1, 1)).flatten()

        sequences.append(seq_scaled)
        scalers.append(scaler)

    return np.array(sequences), scalers, ordered_cols


sequences, scalers, ordered_cols = build_hospital_sequences(df, price_cols, procedure_median)
print("Sequence matrix shape (hospitals x procedures):", sequences.shape)


# =======================================================================================
# 4) SUPERVISED WINDOWING  (sliding window -> next-step forecasting)
# =======================================================================================
WINDOW = 10  # how many prior procedures the model sees before predicting the next one

def make_windows(seqs, window):
    """Turn each hospital's sequence into (X window, y next-value) training pairs."""
    X, y, hosp_idx = [], [], []
    for h, s in enumerate(seqs):
        for t in range(len(s) - window):
            X.append(s[t:t + window])
            y.append(s[t + window])
            hosp_idx.append(h)
    X = np.array(X).reshape(-1, window, 1)   # (samples, timesteps, features)
    y = np.array(y)
    return X, y, np.array(hosp_idx)

X, y, hosp_idx = make_windows(sequences, WINDOW)
print("Total supervised windows:", X.shape)


# =======================================================================================
# 5) TRAIN / TEST SPLIT AT THE HOSPITAL LEVEL (prevents leakage between sets)
# =======================================================================================
n_hospitals = sequences.shape[0]
rng = np.random.default_rng(SEED)
hosp_order = rng.permutation(n_hospitals)
n_test_hosp = max(1, int(0.2 * n_hospitals))
test_hospitals = set(hosp_order[:n_test_hosp])
train_hospitals = set(hosp_order[n_test_hosp:])

train_mask = np.isin(hosp_idx, list(train_hospitals))
test_mask = np.isin(hosp_idx, list(test_hospitals))

X_train, y_train = X[train_mask], y[train_mask]
X_test, y_test = X[test_mask], y[test_mask]

print(f"Train hospitals: {len(train_hospitals)} -> {X_train.shape[0]} windows")
print(f"Test  hospitals: {len(test_hospitals)} -> {X_test.shape[0]} windows")


# =======================================================================================
# 6) MODEL DESIGN — SimpleRNN / LSTM / GRU  (TensorFlow-Keras)
# =======================================================================================
def build_model(cell_type, window):
    """
    Builds a compact 2-layer recurrent network:
      recurrent layer 1 (return_sequences=True) -> Dropout
      recurrent layer 2 (return_sequences=False) -> Dropout
      Dense(16, relu) -> Dense(1, linear)  [regression output: next price, scaled 0-1]
    """
    cell = {"RNN": layers.SimpleRNN, "LSTM": layers.LSTM, "GRU": layers.GRU}[cell_type]

    model = keras.Sequential(name=f"{cell_type}_cost_curve_forecaster")
    model.add(layers.Input(shape=(window, 1)))
    model.add(cell(32, return_sequences=True))
    model.add(layers.Dropout(0.2))
    model.add(cell(16, return_sequences=False))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(16, activation="relu"))
    model.add(layers.Dense(1, activation="linear"))

    model.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3),
                  loss="mse", metrics=["mae"])
    return model


def train_and_evaluate(cell_type):
    tf.random.set_seed(SEED)
    model = build_model(cell_type, WINDOW)

    early_stop = keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=8, restore_best_weights=True
    )

    history = model.fit(
        X_train, y_train,
        validation_split=0.15,
        epochs=100,
        batch_size=32,
        callbacks=[early_stop],
        verbose=0,
    )

    y_pred = model.predict(X_test, verbose=0).flatten()

    metrics = {
        "model": cell_type,
        "MAE": mean_absolute_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "MAPE": np.mean(np.abs((y_test - y_pred) / np.clip(y_test, 1e-6, None))) * 100,
        "R2": r2_score(y_test, y_pred),
        "epochs_trained": len(history.history["loss"]),
    }
    return model, history, y_pred, metrics


results = {}
histories = {}
models = {}
preds = {}

for cell_type in ["RNN", "LSTM", "GRU"]:
    print(f"\nTraining {cell_type} ...")
    model, history, y_pred, metrics = train_and_evaluate(cell_type)
    results[cell_type] = metrics
    histories[cell_type] = history
    models[cell_type] = model
    preds[cell_type] = y_pred
    print(f"  -> MAE={metrics['MAE']:.4f}  RMSE={metrics['RMSE']:.4f}  "
          f"MAPE={metrics['MAPE']:.1f}%%  R2={metrics['R2']:.3f}  "
          f"(stopped after {metrics['epochs_trained']} epochs)")


# =======================================================================================
# 7) MODEL COMPARISON — metrics table + plots
# =======================================================================================
results_df = pd.DataFrame(results).T[["MAE", "RMSE", "MAPE", "R2", "epochs_trained"]]
results_df.to_csv("timeseries_model_comparison.csv")
print("\n================ MODEL COMPARISON (scaled 0-1 price space) ================")
print(results_df.to_string())

# --- 7a. Training/validation loss curves, all 3 models ---
fig, axes = plt.subplots(1, 3, figsize=(16, 4.5), sharey=True)
for ax, cell_type in zip(axes, ["RNN", "LSTM", "GRU"]):
    h = histories[cell_type].history
    ax.plot(h["loss"], label="train loss")
    ax.plot(h["val_loss"], label="val loss")
    ax.set_title(f"{cell_type}")
    ax.set_xlabel("Epoch")
    ax.legend()
axes[0].set_ylabel("MSE Loss")
plt.suptitle("Training Curves — SimpleRNN vs LSTM vs GRU")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/04_training_curves.png", dpi=110)
plt.close()

# --- 7b. Metric comparison bar chart ---
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
for ax, metric in zip(axes, ["MAE", "RMSE", "R2"]):
    sns.barplot(x=results_df.index, y=results_df[metric], hue=results_df.index,
                ax=ax, palette="viridis", legend=False)
    ax.set_title(metric)
plt.suptitle("Model Comparison on Held-Out Hospitals")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/05_metric_comparison.png", dpi=110)
plt.close()

# --- 7c. Actual vs Predicted scatter (best model by R2) ---
best_model_name = results_df["R2"].astype(float).idxmax()
plt.figure(figsize=(6, 6))
plt.scatter(y_test, preds[best_model_name], alpha=0.4, s=15)
lims = [0, 1]
plt.plot(lims, lims, "r--", label="perfect prediction")
plt.xlabel("Actual (scaled price)")
plt.ylabel("Predicted (scaled price)")
plt.title(f"Actual vs Predicted — Best Model: {best_model_name}")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/06_actual_vs_predicted_{best_model_name}.png", dpi=110)
plt.close()

print(f"\nBest model by R2 on the test hospitals: {best_model_name}")




demo_hosp = sorted(test_hospitals)[0]
true_curve = sequences[demo_hosp]
best_model = models[best_model_name]

forecast = list(true_curve[:WINDOW])
window_buf = list(true_curve[:WINDOW])
for _ in range(len(true_curve) - WINDOW):
    x_in = np.array(window_buf[-WINDOW:]).reshape(1, WINDOW, 1)
    next_val = best_model.predict(x_in, verbose=0).flatten()[0]
    forecast.append(next_val)
    window_buf.append(next_val)

plt.figure(figsize=(12, 5))
plt.plot(true_curve, label="Actual cost curve (interpolated)", marker="o", markersize=3)
plt.plot(forecast, label=f"{best_model_name} autoregressive forecast",
         marker="x", markersize=3)
plt.axvline(WINDOW, color="gray", linestyle="--", label="forecast starts here")
plt.title(f"Cost-Curve Forecast/Imputation Demo — {df['hospital'].iloc[demo_hosp]}")
plt.xlabel("Procedure (ordered cheapest -> most expensive)")
plt.ylabel("Scaled price (0-1)")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/07_autoregressive_forecast_demo.png", dpi=110)
plt.close()

print("\nAll plots saved in", PLOT_DIR)
print("Model comparison saved as timeseries_model_comparison.csv")