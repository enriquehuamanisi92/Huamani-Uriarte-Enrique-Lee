# Research Consistency Matrix

## Current implemented benchmark

| Element | Operational formulation |
|---|---|
| Problem | It is unknown whether ML improves next-month forecasting of registered theft and robbery reports in Comas over simple historical baselines. |
| Question | Can temporal ML models outperform persistence and seasonal naive under a final future holdout? |
| Objective | Build a reproducible official-data benchmark and quantify incremental predictive value. |
| Unit | Comas district-month. |
| Outcome | Theft plus robbery reports in month *t + 1*. |
| Predictors | Current category counts, temporal lags, rolling means, trend, time index, and cyclic seasonality. |
| Validation | Train before January 2025; evaluate 16 subsequent forecast months. |
| Metrics | MAE, RMSE, R², and MAPE. |
| Decision | Persistence is retained because all trained models have higher MAE. |

## Full doctoral extension

| Element | Planned formulation |
|---|---|
| Problem | No locally validated model integrates authorized crime history, population exposure, socioeconomic context, and safe geospatial units for Comas. |
| Question | Does multisource integration improve temporal and spatial transfer over crime-history baselines? |
| Unit | Safe intradistrict territory-month, selected after quality and disclosure assessment. |
| Outcome | Next-month property-crime count or exposure-adjusted rate. |
| Validation | Rolling temporal windows, untouched final period, and grouped spatial transfer. |
| Evidence required | Data authorization, provenance, geocoding quality, exposure definition, calibration/uncertainty, external validity, and disparity audit. |

## Objectives, evidence, and status

| Objective | Evidence | Analysis | Status |
|---|---|---|---|
| Document official data | Manifest, license, hash, dictionary | Provenance and schema checks | Completed |
| Characterize district trend | Monthly theft and robbery counts | Time-series plots and summaries | Completed |
| Compare models and baselines | Out-of-time forecasts | Six-method comparison | Completed |
| Test intradistrict spatial transfer | Authorized territorial units | Grouped spatial validation | Pending data |
| Evaluate contextual predictors | Census/urban variables with valid timing | Incremental-value and sensitivity analysis | Pending data |
| Assess territorial disparities | Adequately sized territorial groups | Error, calibration, and uncertainty comparison | Pending data |

The implemented benchmark and full extension are deliberately separated. District-level results are not presented as geospatial validation, and a complex model is not selected merely because it was trained.
