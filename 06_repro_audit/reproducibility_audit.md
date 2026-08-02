# Reproducibility Audit

## Scope

This audit covers the current synthetic artifact. It does not certify the future SIDPOL phase.

| Component | Status | Evidence or pending action |
|---|---|---|
| Data-generation code | Meets current requirement | `05_pipeline/data/create_dataset.py` uses a fixed seed. |
| Temporal split | Partial | Year holdout exists; rolling temporal and spatial tests remain pending. |
| Leakage prevention | Partial | Synthetic lags use `shift`; additional automated tests are required. |
| Dependencies | Partial | `requirements.txt` exists; versions and Python must be pinned. |
| Data | Meets demo requirement | Synthetic CSV and generator are present; real data will never enter the public repository. |
| Experiment tracking | Partial | MLflow was used; raw run stores were removed from Git to reduce noise. |
| Results | Meets demo requirement | Consolidated CSV exists; uncertainty summaries remain pending. |
| Notebook | Partial | Clean end-to-end execution must be independently verified. |
| Container | Partial | Dockerfile exists; automated build verification is pending. |
| Artifact integrity | Pending | Record SHA-256 values for data, configuration, and commit. |
| Independent reproduction | Pending | A second person must clone and document the actual result. |

## Clean-clone test

1. Clone a tagged version.
2. Create an environment with the documented Python version.
3. Install dependencies without manual changes.
4. Regenerate the synthetic CSV.
5. Run experiments and compare rows, models, and metric tolerances.
6. Record operating system, Python version, runtime, commit, and differences.

## Principal finding

Current values show that the software processes synthetic data; they do not establish external validity. Curated summaries should remain in `docs/`, while extensive artifacts should be handled through DVC or institutional storage.
