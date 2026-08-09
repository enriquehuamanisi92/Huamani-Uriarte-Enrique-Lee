# Reproducibility Audit — Official Comas SIDPOL Experiment

## Scope

This audit covers the completed district-level forecasting experiment in `05_pipeline/`. It verifies data provenance, deterministic processing, temporal validation, saved outputs, and automated tests. It does not certify operational deployment or intradistrict geospatial performance.

## Audit findings

| Domain | Status | Evidence |
|---|---|---|
| Public-data provenance | Meets | `docs/source_manifest.csv` records publisher, source URL, license, download date, size, and SHA-256 hash. |
| Geographic scope | Meets | Comas is selected through UBIGEO `150110`; tests verify the 101-month series. |
| Outcome definition | Meets | Theft plus robbery reports in the following month; other categories are excluded. |
| Leakage prevention | Meets for implemented features | Lags and rolling means use `shift`; the target uses a one-month negative shift. |
| Temporal validation | Meets | Training features precede January 2025; the final 16 forecast months are held out. |
| Baseline comparison | Meets | Persistence and 12-month seasonal-naive baselines are evaluated on identical months. |
| Seed control | Meets | Random forest is repeated with seeds 13, 21, 42, 87, and 100. |
| Saved results | Meets | Seed-level metrics, mean comparison, month-level forecasts, figures, and notebook outputs are versioned. |
| Automated tests | Meets | Tests verify scope, total reports, chronological uniqueness, and complete features/target. |
| Clean execution | Meets locally | Training, repeated experiments, figure generation, tests, and the notebook completed without model-code errors. |
| External validation | Not met | The experiment covers one district and no independent city or later data release. |
| Spatial validation | Not applicable to current public table | The source contains district-month aggregates and no intradistrict units. |
| Operational validation | Not met | No institutional pilot, intervention evaluation, or deployment authorization exists. |

## Reproduction commands

```powershell
cd 05_pipeline
py -3 -m pip install -r requirements.txt
py -3 src/run_experiments.py
py -3 src/make_figures.py
py -3 -m unittest discover -s ..\tests -p "test_*.py"
```

Expected core assertions:

- 101 monthly periods from January 2018 through May 2026;
- 47,554 combined theft and robbery reports;
- 72 training rows and 16 test rows after feature construction;
- persistence is the best tested model with MAE 37.19.

## Reproducibility limitations

The national source file may be revised by its publisher. Reproduction of this exact version therefore requires the repository copy or a file matching SHA-256 `CDC6D3D32A37A00FF7F2F1D15D65512FEC3A36A0291BB67FEDE482CA1FFB22BC`. Reproducibility does not establish representativeness, causality, fairness, external validity, or institutional utility.
