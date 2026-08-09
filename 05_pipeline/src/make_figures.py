"""Generate presentation figures from the official Comas series and saved results."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
sys.path.insert(0, str(ROOT / "src"))
from train import TEST_START, load_comas_monthly_data  # noqa: E402


plt.style.use("seaborn-v0_8-whitegrid")


def save_history():
    data = load_comas_monthly_data()
    fig, ax = plt.subplots(figsize=(12, 5.5))
    ax.plot(data["date"], data["theft_reports"], label="Theft", linewidth=1.7)
    ax.plot(data["date"], data["robbery_reports"], label="Robbery", linewidth=1.7)
    ax.plot(data["date"], data["property_crime_reports"], label="Combined", linewidth=2.5, color="#111827")
    ax.axvline(TEST_START, color="#dc2626", linestyle="--", label="Test period begins")
    ax.set(title="Monthly Police Reports in Comas (UBIGEO 150110)", xlabel="Month", ylabel="Registered reports")
    ax.legend(ncol=4, frameon=True)
    fig.tight_layout()
    fig.savefig(DOCS / "monthly_property_crime_history.png", dpi=180)
    plt.close(fig)


def save_forecasts():
    data = pd.read_csv(DOCS / "test_period_forecasts.csv", parse_dates=["forecast_month"])
    fig, ax = plt.subplots(figsize=(12, 5.5))
    ax.plot(data["forecast_month"], data["observed"], marker="o", linewidth=2.5, color="#111827", label="Observed")
    ax.plot(data["forecast_month"], data["persistence_baseline"], marker="o", label="Persistence")
    ax.plot(data["forecast_month"], data["ridge_regression"], marker="o", label="Ridge")
    ax.plot(data["forecast_month"], data["random_forest"], marker="o", label="Random forest")
    ax.set(title="Out-of-Time Forecasts: February 2025–May 2026", xlabel="Forecast month", ylabel="Theft + robbery reports")
    ax.legend(ncol=4, frameon=True)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(DOCS / "test_period_forecasts.png", dpi=180)
    plt.close(fig)


def save_comparison():
    data = pd.read_csv(DOCS / "model_comparison.csv").sort_values("mae_mean", ascending=True)
    labels = data["model"].str.replace("_", " ").str.title()
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["#16a34a" if name == "persistence_baseline" else "#2563eb" for name in data["model"]]
    bars = ax.barh(labels, data["mae_mean"], color=colors)
    ax.bar_label(bars, fmt="%.2f", padding=4)
    ax.set(title="Model Comparison on the Final Temporal Holdout", xlabel="Mean absolute error (lower is better)", ylabel="")
    ax.set_xlim(0, data["mae_mean"].max() * 1.18)
    fig.tight_layout()
    fig.savefig(DOCS / "model_mae_comparison.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    DOCS.mkdir(parents=True, exist_ok=True)
    save_history()
    save_forecasts()
    save_comparison()
    print("Saved three figures to", DOCS)
