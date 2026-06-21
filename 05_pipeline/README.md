# Comas Urban Crime Risk - Reproducible Baseline Pipeline

Reproducible baseline pipeline for the project **Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Lima Metropolitana**.

**Author:** Enrique Lee Huamani Uriarte  
**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies - UNMSM

## Purpose Of This Folder

This folder is the technical artifact for the course repository. It demonstrates a reproducibility stack for an applied urban analytics project using a small **synthetic SIDPOL-like and census-like dataset**.

The goal is modest but important: show how the future research workflow can track data, train models, record experiments, document the environment, and be rerun in a clean way before real institutional data are introduced.

## Recommended Environment

The recommended environment for the teaching artifact is **Google Colab**, because it makes the workflow easy to demonstrate without local setup. Local execution is also supported.

Open the notebook directly in Colab:

[Open in Colab](https://colab.research.google.com/github/enrique-lee-huamani-uriarte/comas-urban-crime-risk/blob/main/05_pipeline/notebook.ipynb)

Update the link if the repository is published under a different GitHub user or repository name.

## What Is Included

- `data/create_dataset.py` - creates the synthetic territorial-time dataset
- `data/comas_urban_crime_synthetic.csv.dvc` - DVC pointer for the tracked synthetic dataset
- `data/comas_urban_crime_synthetic.csv` - generated synthetic dataset used by the baseline
- `src/train.py` - runs one temporal-holdout baseline experiment
- `src/run_experiments.py` - runs the multi-seed experiment set and logs results
- `docs/experiment_results.csv` - saved experiment summary
- `notebook.ipynb` - Colab-friendly notebook for setup, inspection, and demonstration
- `mlruns/` - MLflow tracking output generated for the current baseline
- `Dockerfile` - environment description for container-based reproduction

## Important Limitation

`data/comas_urban_crime_synthetic.csv` is a synthetic teaching dataset. It does **not** contain real SIDPOL records, real police complaints, real victim information, or operational municipal data. It must not be used for public-safety decisions.

The synthetic data imitate the structure of a possible Comas crime-risk dataset: territorial cells, monthly observations, geospatial coordinates, socioeconomic indicators, urban infrastructure proxies, recent incident pressure, and a next-month high-risk label.

## Google Colab Workflow

1. Open `05_pipeline/notebook.ipynb` from GitHub or by using the Colab link above.
2. Run the setup cells that clone the repository and install dependencies.
3. Move into the `05_pipeline/` folder inside the Colab runtime.
4. Inspect the synthetic dataset and saved experiment results.
5. Run `src/train.py` for one baseline experiment or `src/run_experiments.py` for the full multi-seed workflow.

If Colab shows a warning about preinstalled packages after installation, restart the runtime once and run the notebook again from the top.

## Local Reproduction Workflow

Recommended on Windows: use Python 3.12.

1. Create the environment

```bash
uv venv --python 3.12 .venv
```

2. Install dependencies

```bash
uv pip install --python .venv -r requirements.txt
```

3. Regenerate the synthetic dataset

```bash
.\.venv\Scripts\python data/create_dataset.py
```

4. Run one temporal-holdout model training

```bash
.\.venv\Scripts\python src/train.py --seed 42 --holdout_year 2024
```

5. Run the full experiment set and generate MLflow runs

```bash
.\.venv\Scripts\python src/run_experiments.py
```

6. Open the MLflow UI

```bash
.\.venv\Scripts\mlflow ui --backend-store-uri .\mlruns
```

Then open `http://127.0.0.1:5000`.

## DVC Configuration

This project is prepared to use a DVC remote for data tracking. The current dataset is synthetic and small enough to remain in the repository for demonstration, but the `.dvc` pointer documents how larger data artifacts should be tracked.

For real SIDPOL or institutional datasets, do not commit raw files. Use access-controlled storage, anonymization, aggregation, and a documented DVC remote approved by the responsible institution.

## Current Baseline

The current baseline predicts `target_high_risk_next_month` using a temporal split:

- training period: synthetic observations before `2024`
- holdout period: synthetic observations from `2024` onward
- classification threshold: training-set high-risk prevalence, used as a transparent operating point for screening

Models currently compared:

- logistic regression
- random forest
- histogram gradient boosting
- support vector machine with RBF kernel
- multilayer perceptron neural network

Metrics currently saved:

- AUC-ROC
- PR-AUC
- accuracy
- precision
- recall
- F1-score

## Docker Note

The Dockerfile documents a Python 3.12 environment for reproducibility. If Docker is available, build from this folder:

```bash
docker build -t comas-urban-crime-risk .
```

Then run:

```bash
docker run --rm -it comas-urban-crime-risk
```

Docker execution should be validated again when the final repository is published.
