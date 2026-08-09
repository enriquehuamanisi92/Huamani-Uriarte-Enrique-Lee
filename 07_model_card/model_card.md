# Model Card — Comas Monthly Property-Crime Forecasting Benchmark

## Model details

- **Developer:** Enrique Lee Huamani Uriarte.
- **Version:** 1.0-public-district-benchmark.
- **Date:** August 2026.
- **Status:** completed research benchmark; not approved for operational use.
- **Geographic scope:** Comas District, Metropolitan Lima, UBIGEO `150110`.
- **Temporal scope:** source data from January 2018 through May 2026.

## Intended purpose

The pipeline evaluates whether lagged, seasonal, and trend features improve next-month forecasting of aggregated theft and robbery reports in Comas. It is intended for doctoral research, methodological evaluation, and reproducibility training.

It is not intended to:

- predict individuals, offending, guilt, victimization, or recidivism;
- direct patrols or allocate enforcement resources automatically;
- estimate unreported crime or causal effects;
- produce neighborhood risk maps from district-level data;
- justify labeling any community as inherently dangerous.

## Data

The source is the public Ministry of the Interior Police Reports Dataset derived from SIDPOL. The published table is aggregated by month, geography, category, and count and contains no personal identifiers or point coordinates. The implemented outcome contains 47,554 theft and robbery reports over 101 months.

Registered reports are an imperfect measurement of crime because they also reflect reporting access, willingness to report, classification, and institutional recording practices.

## Models and evaluation

The study compares persistence, 12-month seasonal naive, linear regression, ridge regression, random forest, and histogram gradient boosting. Models train on historical rows before January 2025 and are evaluated on 16 future forecast months.

| Model | MAE | RMSE | R² | MAPE |
|---|---:|---:|---:|---:|
| Persistence | **37.19** | **44.95** | **0.141** | **11.05%** |
| Ridge regression | 43.11 | 50.71 | -0.093 | 13.04% |
| Random forest | 46.99 | 56.70 | -0.368 | 15.00% |
| Linear regression | 47.11 | 54.85 | -0.279 | 14.38% |
| Histogram gradient boosting | 56.14 | 68.57 | -0.999 | 17.88% |
| Seasonal naive | 143.81 | 167.14 | -10.878 | 41.14% |

## Performance decision

Persistence is the selected benchmark because it has the lowest test MAE. No trained machine-learning model demonstrated sufficient incremental value. The project therefore does not recommend deployment of a complex model from the current evidence.

## Limitations and risks

- one district and a small monthly sample;
- structural disruption around COVID-19 and later temporal drift;
- no population exposure, mobility, socioeconomic, or built-environment predictors in the implemented table;
- no intradistrict or external validation;
- potential feedback, stigma, and false-confidence risks if forecasts are operationalized;
- prediction of registered reports rather than complete underlying crime.

## Release requirements for any future pilot

Any status change requires institutional authorization, applicable ethics review, lawful and documented data access, meaningful baselines, calibration and uncertainty analysis, spatial and temporal external validation, disparity auditing, human oversight, monitoring, correction procedures, and explicit withdrawal criteria.
