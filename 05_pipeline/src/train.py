import argparse
import random
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC

try:
    import mlflow
    import mlflow.sklearn

    MLFLOW_AVAILABLE = True
except Exception:
    MLFLOW_AVAILABLE = False


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "comas_urban_crime_synthetic.csv"


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)


def build_preprocessor():
    numeric_features = [
        "latitude",
        "longitude",
        "year",
        "month",
        "month_index",
        "population_density_km2",
        "socioeconomic_vulnerability",
        "youth_share",
        "commercial_density",
        "transit_access_index",
        "road_connectivity_index",
        "lighting_coverage",
        "cctv_density",
        "patrol_coverage",
        "distance_to_transit_corridor_km",
        "weekend_night_activity",
        "seasonal_pressure",
        "recent_incidents",
        "rolling_3m_incidents",
        "incident_trend",
    ]
    categorical_features = ["sector"]

    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )


def prepare_temporal_split(df: pd.DataFrame, holdout_year: int):
    target = "target_high_risk_next_month"
    drop_columns = [target, "zone_id"]

    train_df = df[df["year"] < holdout_year].copy()
    test_df = df[df["year"] >= holdout_year].copy()

    if train_df.empty or test_df.empty:
        raise ValueError("Temporal split produced an empty train or test set.")

    X_train = train_df.drop(columns=drop_columns)
    y_train = train_df[target]
    X_test = test_df.drop(columns=drop_columns)
    y_test = test_df[target]

    return X_train, X_test, y_train, y_test


def build_models(seed: int):
    return {
        "logistic_regression": LogisticRegression(
            max_iter=1500,
            class_weight="balanced",
            random_state=seed,
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=350,
            min_samples_leaf=6,
            class_weight="balanced",
            random_state=seed,
            n_jobs=-1,
        ),
        "gradient_boosting": HistGradientBoostingClassifier(
            learning_rate=0.06,
            max_iter=220,
            max_leaf_nodes=31,
            random_state=seed,
        ),
        "svm_rbf": CalibratedClassifierCV(
            estimator=SVC(
                C=2.0,
                gamma="scale",
                class_weight="balanced",
            ),
            method="sigmoid",
            cv=3,
        ),
        "mlp_neural_net": MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            alpha=0.001,
            early_stopping=True,
            max_iter=300,
            random_state=seed,
        ),
    }


def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    pipe = Pipeline(
        steps=[
            ("preprocess", build_preprocessor()),
            ("model", model),
        ]
    )
    pipe.fit(X_train, y_train)

    y_prob = pipe.predict_proba(X_test)[:, 1]
    classification_threshold = float(y_train.mean())
    y_pred = (y_prob >= classification_threshold).astype(int)

    metrics = {
        "model": name,
        "classification_threshold": classification_threshold,
        "auc_roc": float(roc_auc_score(y_test, y_prob)),
        "pr_auc": float(average_precision_score(y_test, y_prob)),
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
    }

    return pipe, metrics


def main(seed: int, holdout_year: int = 2024):
    set_seed(seed)

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. Run `python data/create_dataset.py` first."
        )

    # Synthetic territorial-time data to validate the reproducibility stack.
    # This is not real SIDPOL, municipal, census, or police-operational data.
    df = pd.read_csv(DATA_PATH)
    X_train, X_test, y_train, y_test = prepare_temporal_split(df, holdout_year=holdout_year)

    fitted = {}
    results = []

    for name, model in build_models(seed).items():
        fitted_model, metrics = evaluate_model(name, model, X_train, X_test, y_train, y_test)
        fitted[name] = fitted_model
        results.append(metrics)
        print(
            f"[{name}] seed={seed} holdout_year={holdout_year} "
            f"Threshold={metrics['classification_threshold']:.4f} "
            f"AUC-ROC={metrics['auc_roc']:.4f} "
            f"PR-AUC={metrics['pr_auc']:.4f} "
            f"Accuracy={metrics['accuracy']:.4f} "
            f"Precision={metrics['precision']:.4f} "
            f"Recall={metrics['recall']:.4f} "
            f"F1={metrics['f1']:.4f}"
        )

    return fitted, results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--holdout_year", type=int, default=2024)
    args = parser.parse_args()
    main(seed=args.seed, holdout_year=args.holdout_year)
