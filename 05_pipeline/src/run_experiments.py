import os
from pathlib import Path

import pandas as pd

from train import MLFLOW_AVAILABLE, main

if MLFLOW_AVAILABLE:
    import mlflow


SEEDS = [13, 21, 42, 87, 100]
HOLDOUT_YEAR = 2024
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "docs" / "experiment_results.csv"
TRACKING_PATH = PROJECT_ROOT / "mlruns"
LOG_MODELS = os.getenv("MLFLOW_LOG_MODELS", "0") == "1"
os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")


def run():
    all_rows = []

    if MLFLOW_AVAILABLE:
        mlflow.set_tracking_uri(TRACKING_PATH.resolve().as_uri())
        mlflow.set_experiment("comas-urban-crime-risk-baseline")
        print(f"MLflow tracking URI: {TRACKING_PATH}")

    for seed in SEEDS:
        fitted, results = main(seed=seed, holdout_year=HOLDOUT_YEAR)

        for row in results:
            out_row = {"seed": seed, "holdout_year": HOLDOUT_YEAR, **row}
            all_rows.append(out_row)

            if MLFLOW_AVAILABLE:
                with mlflow.start_run(run_name=f"{row['model']}-seed-{seed}"):
                    mlflow.log_param("seed", seed)
                    mlflow.log_param("model", row["model"])
                    mlflow.log_param("holdout_year", HOLDOUT_YEAR)
                    mlflow.log_param("classification_threshold", row["classification_threshold"])
                    for metric_name in [
                        "auc_roc",
                        "pr_auc",
                        "accuracy",
                        "precision",
                        "recall",
                        "f1",
                    ]:
                        mlflow.log_metric(metric_name, row[metric_name])
                    mlflow.set_tag("project", "comas-urban-crime-risk")
                    mlflow.set_tag("data_type", "synthetic")
                    mlflow.set_tag("model_artifact_logging", "enabled" if LOG_MODELS else "disabled")
                    if LOG_MODELS:
                        mlflow.sklearn.log_model(fitted[row["model"]], "model")

    df = pd.DataFrame(all_rows)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved experiment summary to: {OUTPUT_PATH}")


if __name__ == "__main__":
    run()
