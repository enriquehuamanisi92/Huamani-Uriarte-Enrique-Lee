"""Train and evaluate monthly property-crime forecasts for Comas using public SIDPOL data."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "sidpol_police_reports_2018_2026.csv"
COMAS_UBIGEO = "150110"
PROPERTY_CRIME_CATEGORIES = {"Hurto": "theft_reports", "Robo": "robbery_reports"}
TEST_START = pd.Timestamp("2025-01-01")


def load_comas_monthly_data(path: Path = DATA_PATH) -> pd.DataFrame:
    raw = pd.read_csv(path, dtype={"UBIGEO_HECHO": str})
    raw["UBIGEO_HECHO"] = raw["UBIGEO_HECHO"].str.zfill(6)
    selected = raw[
        (raw["UBIGEO_HECHO"] == COMAS_UBIGEO)
        & raw["P_MODALIDADES"].isin(PROPERTY_CRIME_CATEGORIES)
    ].copy()
    if selected.empty:
        raise ValueError("No Comas property-crime records were found in the official dataset.")

    selected["date"] = pd.to_datetime(
        dict(year=selected["ANIO"], month=selected["MES"], day=1)
    )
    monthly = selected.pivot_table(
        index="date", columns="P_MODALIDADES", values="cantidad", aggfunc="sum", fill_value=0
    ).rename(columns=PROPERTY_CRIME_CATEGORIES)
    complete_index = pd.date_range(monthly.index.min(), monthly.index.max(), freq="MS")
    monthly = monthly.reindex(complete_index, fill_value=0).rename_axis("date").reset_index()
    monthly["property_crime_reports"] = monthly[list(PROPERTY_CRIME_CATEGORIES.values())].sum(axis=1)
    return monthly


def build_features(monthly: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    df = monthly.copy()
    df["time_index"] = np.arange(len(df))
    df["month_sin"] = np.sin(2 * np.pi * df["date"].dt.month / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["date"].dt.month / 12)
    for lag in (1, 2, 3, 6, 12):
        df[f"lag_{lag}"] = df["property_crime_reports"].shift(lag)
    df["rolling_mean_3"] = df["property_crime_reports"].shift(1).rolling(3).mean()
    df["rolling_mean_6"] = df["property_crime_reports"].shift(1).rolling(6).mean()
    df["recent_trend"] = df["lag_1"] - df["lag_3"]
    df["target_next_month"] = df["property_crime_reports"].shift(-1)
    features = [
        "time_index", "month_sin", "month_cos", "property_crime_reports",
        "theft_reports", "robbery_reports", "lag_1", "lag_2", "lag_3",
        "lag_6", "lag_12", "rolling_mean_3", "rolling_mean_6", "recent_trend",
    ]
    return df.dropna(subset=features + ["target_next_month"]).copy(), features


def models(seed: int):
    return {
        "linear_regression": Pipeline([("scale", StandardScaler()), ("model", LinearRegression())]),
        "ridge_regression": Pipeline([("scale", StandardScaler()), ("model", Ridge(alpha=10.0))]),
        "random_forest": RandomForestRegressor(
            n_estimators=500, min_samples_leaf=3, max_features=0.8,
            random_state=seed, n_jobs=-1,
        ),
        "hist_gradient_boosting": HistGradientBoostingRegressor(
            learning_rate=0.05, max_iter=250, max_leaf_nodes=15,
            l2_regularization=2.0, random_state=seed,
        ),
    }


def metrics(y_true, y_pred) -> dict[str, float]:
    y_pred = np.maximum(np.asarray(y_pred, dtype=float), 0)
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "r2": float(r2_score(y_true, y_pred)),
        "mape_pct": float(np.mean(np.abs((np.asarray(y_true) - y_pred) / np.asarray(y_true))) * 100),
    }


def run_training(seed: int = 42):
    monthly = load_comas_monthly_data()
    frame, feature_names = build_features(monthly)
    train = frame[frame["date"] < TEST_START]
    test = frame[frame["date"] >= TEST_START]
    if train.empty or test.empty:
        raise ValueError("Temporal split produced an empty training or test set.")

    X_train, y_train = train[feature_names], train["target_next_month"]
    X_test, y_test = test[feature_names], test["target_next_month"]
    results, predictions, fitted = [], {}, {}

    baselines = {
        "persistence_baseline": test["property_crime_reports"].to_numpy(),
        "seasonal_naive_12m": test["lag_12"].to_numpy(),
    }
    for name, prediction in baselines.items():
        predictions[name] = prediction
        results.append({"model": name, "seed": seed, **metrics(y_test, prediction)})

    for name, model in models(seed).items():
        model.fit(X_train, y_train)
        prediction = np.maximum(model.predict(X_test), 0)
        fitted[name] = model
        predictions[name] = prediction
        results.append({"model": name, "seed": seed, **metrics(y_test, prediction)})

    prediction_frame = pd.DataFrame({
        "feature_month": test["date"].dt.strftime("%Y-%m"),
        "forecast_month": (test["date"] + pd.offsets.MonthBegin(1)).dt.strftime("%Y-%m"),
        "observed": y_test.astype(int).to_numpy(),
        **{name: np.round(values, 2) for name, values in predictions.items()},
    })
    metadata = {
        "raw_rows": 698,
        "monthly_periods": len(monthly),
        "property_crime_reports": int(monthly["property_crime_reports"].sum()),
        "training_rows": len(train),
        "test_rows": len(test),
        "data_start": monthly["date"].min().strftime("%Y-%m"),
        "data_end": monthly["date"].max().strftime("%Y-%m"),
    }
    return pd.DataFrame(results), prediction_frame, metadata, fitted


if __name__ == "__main__":
    result, forecasts, info, _ = run_training()
    print(pd.DataFrame([info]).to_string(index=False))
    print(result.sort_values("mae").to_string(index=False))
    print(forecasts.to_string(index=False))
