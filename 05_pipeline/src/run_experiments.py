"""Run repeated real-data experiments and save auditable result tables."""

from pathlib import Path

import pandas as pd

from train import run_training


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"
SEEDS = [13, 21, 42, 87, 100]


def run():
    DOCS.mkdir(parents=True, exist_ok=True)
    all_results = []
    canonical_forecasts = None
    metadata = None
    for seed in SEEDS:
        results, forecasts, metadata, _ = run_training(seed=seed)
        all_results.append(results)
        if seed == 42:
            canonical_forecasts = forecasts

    experiments = pd.concat(all_results, ignore_index=True)
    experiments.to_csv(DOCS / "experiment_results.csv", index=False)
    canonical_forecasts.to_csv(DOCS / "test_period_forecasts.csv", index=False)
    pd.DataFrame([metadata]).to_csv(DOCS / "real_data_summary.csv", index=False)

    summary = experiments.groupby("model").agg(
        mae_mean=("mae", "mean"), mae_sd=("mae", "std"),
        rmse_mean=("rmse", "mean"), r2_mean=("r2", "mean"),
        mape_pct_mean=("mape_pct", "mean"),
    ).sort_values("mae_mean")
    summary.to_csv(DOCS / "model_comparison.csv")
    print(summary.to_string())


if __name__ == "__main__":
    run()
