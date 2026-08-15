#Top 10 heath care companies DL
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

FILE = "Top 10 Healthcare Companies in the United States.xlsx"
PLOT_DIR = "plots_stocks_ts"
os.makedirs(PLOT_DIR, exist_ok=True)


# =======================================================================================
# 1) LOAD & CLEAN
# =======================================================================================

def load_all_companies(path):
    x1 = pd.ExcelFile(path)
    close_frames = {}
    for sheet in x1.sheet_names:  
        raw = pd.read_excel(x1, sheet_name=sheet, skiprows=4,
                            names=["Date", "Close", "High", "Low", "Volume"])
        raw = raw.dropna(subset=["Date"])
        raw["Date"] = pd.to_datetime(
            raw["Date"].str.split(" 오").str[0].str.strip(), format="%Y. %m. %d"
        )
        ticker = sheet.split("(")[-1].replace(")", "").strip() if "(" in sheet else "WBA"
        close_frames[ticker] = raw.set_index("Date")["Close"]
    merged = pd.DataFrame(close_frames).sort_index()
    return merged


prices = load_all_companies(FILE).ffill().dropna()
companies = prices.columns.tolist()
print("Price table:", prices.shape, "| Companies:", companies)


# =======================================================================================
# 2) EDA
# =======================================================================================
# --- daily returns (%) distribution, a standard finance-time-series diagnostic ---
returns = prices.pct_change().dropna() * 100

plt.figure(figsize=(12, 5))
sns.boxplot(data=returns, palette="Set2")
plt.title("Daily Return (%) Distribution — Volatility Comparison Across Companies")
plt.ylabel("Daily Return (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/01_daily_return_volatility.png", dpi=110)
plt.close()

# --- rolling 60-day volatility for all companies ---
plt.figure(figsize=(13, 5))
rolling_vol = returns.rolling(60).std()
for c in companies:
    plt.plot(rolling_vol.index, rolling_vol[c], label=c, linewidth=0.9)
plt.title("60-Day Rolling Volatility")
plt.legend(fontsize=7, ncol=2)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/02_rolling_volatility.png", dpi=110)
plt.close()

print("EDA plots saved to", PLOT_DIR)


# =======================================================================================
# 3) SCALING + SLIDING-WINDOW DATASET  (per-company MinMax scaling)
# =======================================================================================
WINDOW = 60  # look back 60 trading days (~3 months) to predict the next day's close

HOLDOUT_COMPANY = "CNC"   # completely unseen during training -> genuine generalisation test
train_companies = [c for c in companies if c != HOLDOUT_COMPANY]

scalers = {}


def make_company_windows(series, window):
    """Scale one company's price series to [0,1] and build sliding-window samples,
    split CHRONOLOGICALLY (first 80% of time = train, last 20% = test)."""
    values = series.values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(values).flatten()

    X, y = [], []
    for t in range(len(scaled) - window):
        X.append(scaled[t:t + window])
        y.append(scaled[t + window])
    X = np.array(X).reshape(-1, window, 1)
    y = np.array(y)

    split = int(len(X) * 0.8)
    return X[:split], y[:split], X[split:], y[split:], scaler


X_train_list, y_train_list, X_test_list, y_test_list = [], [], [], []
for c in train_companies:
    Xtr, ytr, Xte, yte, scaler = make_company_windows(prices[c], WINDOW)
    X_train_list.append(Xtr); y_train_list.append(ytr)
    X_test_list.append(Xte); y_test_list.append(yte)
    scalers[c] = scaler

X_train = np.concatenate(X_train_list)
y_train = np.concatenate(y_train_list)
X_test = np.concatenate(X_test_list)
y_test = np.concatenate(y_test_list)

# holdout company: build its own windows + scaler too (used only for the bonus demo)
Xh_train, yh_train, Xh_test, yh_test, holdout_scaler = make_company_windows(
    prices[HOLDOUT_COMPANY], WINDOW
)
scalers[HOLDOUT_COMPANY] = holdout_scaler

print(f"Train windows (9 companies, chronological 80%): {X_train.shape}")
print(f"Test windows  (9 companies, chronological last 20%): {X_test.shape}")
print(f"Held-out company '{HOLDOUT_COMPANY}' windows (never trained on): {Xh_test.shape}")


# =======================================================================================
# 4) MODEL DESIGN — SimpleRNN / LSTM / GRU
# =======================================================================================
def build_model(cell_type, window):
    cell = {"RNN": layers.SimpleRNN, "LSTM": layers.LSTM, "GRU": layers.GRU}[cell_type]
    model = keras.Sequential(name=f"{cell_type}_stock_forecaster")
    model.add(layers.Input(shape=(window, 1)))
    model.add(cell(64, return_sequences=True))
    model.add(layers.Dropout(0.2))
    model.add(cell(32, return_sequences=False))
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
        monitor="val_loss", patience=5, restore_best_weights=True
    )
    history = model.fit(
        X_train, y_train,
        validation_split=0.1,
        epochs=40,
        batch_size=64,
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

    # also score on the fully held-out company (never seen in training)
    yh_pred = model.predict(Xh_test, verbose=0).flatten()
    metrics["holdout_R2"] = r2_score(yh_test, yh_pred)
    metrics["holdout_MAE"] = mean_absolute_error(yh_test, yh_pred)

    return model, history, y_pred, yh_pred, metrics


results, histories, models, preds, holdout_preds = {}, {}, {}, {}, {}
for cell_type in ["RNN", "LSTM", "GRU"]:
    print(f"\nTraining {cell_type} ...")
    model, history, y_pred, yh_pred, metrics = train_and_evaluate(cell_type)
    results[cell_type] = metrics
    histories[cell_type] = history
    models[cell_type] = model
    preds[cell_type] = y_pred
    holdout_preds[cell_type] = yh_pred
    print(f"  -> Test: MAE={metrics['MAE']:.4f} RMSE={metrics['RMSE']:.4f} "
          f"MAPE={metrics['MAPE']:.1f}% R2={metrics['R2']:.3f} | "
          f"Holdout({HOLDOUT_COMPANY}) R2={metrics['holdout_R2']:.3f} "
          f"(stopped after {metrics['epochs_trained']} epochs)")


# =======================================================================================
# 5) MODEL COMPARISON
# =======================================================================================
results_df = pd.DataFrame(results).T[
    ["MAE", "RMSE", "MAPE", "R2", "holdout_MAE", "holdout_R2", "epochs_trained"]
]
results_df.to_csv("stocks_timeseries_model_comparison.csv")
print("\n================ MODEL COMPARISON (scaled 0-1 price space) ================")
print(results_df.to_string())

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5), sharey=True)
for ax, cell_type in zip(axes, ["RNN", "LSTM", "GRU"]):
    h = histories[cell_type].history
    ax.plot(h["loss"], label="train loss")
    ax.plot(h["val_loss"], label="val loss")
    ax.set_title(cell_type); ax.set_xlabel("Epoch"); ax.legend()
axes[0].set_ylabel("MSE Loss")
plt.suptitle("Training Curves — SimpleRNN vs LSTM vs GRU")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/03_training_curves.png", dpi=110)
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
for ax, metric in zip(axes, ["MAE", "RMSE", "R2"]):
    vals = results_df[metric].astype(float)
    sns.barplot(x=vals.index, y=vals.values, hue=vals.index, ax=ax,
                palette="viridis", legend=False)
    ax.set_title(metric)
plt.suptitle("Model Comparison on Chronological Test Set")
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/04_metric_comparison.png", dpi=110)
plt.close()

best_model_name = results_df["R2"].astype(float).idxmax()
print(f"\nBest model by test R2: {best_model_name}")

plt.figure(figsize=(6, 6))
plt.scatter(y_test, preds[best_model_name], alpha=0.15, s=8)
plt.plot([0, 1], [0, 1], "r--", label="perfect prediction")
plt.xlabel("Actual (scaled price)"); plt.ylabel("Predicted (scaled price)")
plt.title(f"Actual vs Predicted — {best_model_name} (all 9 training companies, test period)")
plt.legend(); plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/05_actual_vs_predicted_{best_model_name}.png", dpi=110)
plt.close()


# =======================================================================================
# 6) BONUS — HELD-OUT COMPANY (never trained on) + multi-step-ahead forecast demo
# =======================================================================================
best_model = models[best_model_name]

# 6a. one-step predictions on the held-out company's whole test window
plt.figure(figsize=(12, 5))
plt.plot(yh_test, label=f"Actual {HOLDOUT_COMPANY} (scaled)", linewidth=1)
plt.plot(holdout_preds[best_model_name], label=f"{best_model_name} predicted", linewidth=1)
plt.title(f"Zero-Shot Generalisation Test: {best_model_name} trained on 9 companies,\n"
          f"predicting {HOLDOUT_COMPANY} which it NEVER saw during training "
          f"(Holdout R2={results[best_model_name]['holdout_R2']:.3f})")
plt.xlabel("Test day index"); plt.ylabel("Scaled close price")
plt.legend(); plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/06_holdout_company_zero_shot.png", dpi=110)
plt.close()

# 6b. genuine 30-trading-day-ahead AUTOREGRESSIVE forecast on the held-out company
FORECAST_HORIZON = 30
scaled_full = holdout_scaler.transform(prices[[HOLDOUT_COMPANY]].values).flatten()
seed_window = list(scaled_full[-(WINDOW + FORECAST_HORIZON):-FORECAST_HORIZON])
actual_future = scaled_full[-FORECAST_HORIZON:]

forecast = []
buf = seed_window.copy()
for _ in range(FORECAST_HORIZON):
    x_in = np.array(buf[-WINDOW:]).reshape(1, WINDOW, 1)
    next_val = best_model.predict(x_in, verbose=0).flatten()[0]
    forecast.append(next_val)
    buf.append(next_val)

plt.figure(figsize=(10, 5))
plt.plot(range(FORECAST_HORIZON), actual_future, label="Actual (last 30 trading days)",
         marker="o", markersize=3)
plt.plot(range(FORECAST_HORIZON), forecast, label=f"{best_model_name} 30-day forecast",
         marker="x", markersize=3)
plt.title(f"{FORECAST_HORIZON}-Trading-Day-Ahead Autoregressive Forecast — {HOLDOUT_COMPANY}")
plt.xlabel("Trading days into the future"); plt.ylabel("Scaled close price")
plt.legend(); plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/07_30day_autoregressive_forecast.png", dpi=110)
plt.close()

print("\nAll plots saved in", PLOT_DIR)
print("Model comparison saved as stocks_timeseries_model_comparison.csv")