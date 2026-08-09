# Research Protocol v1.0 — Updated Evidence Status

**Title:** Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Metropolitan Lima

**Version:** 1.0, amended August 9, 2026

**Author:** Enrique Lee Huamani Uriarte

## 1. Problem statement

Police reports, population exposure, socioeconomic conditions, and the urban environment describe complementary dimensions of recorded crime risk, but they are commonly fragmented and available at different spatial and temporal resolutions. The research problem is the absence of a locally validated, reproducible, and responsible next-period forecasting model for Comas that demonstrates incremental value over simple baselines without equating registered reports with all crime or predictive associations with causality.

The repository now contains a completed district-level benchmark using public Ministry of the Interior/SIDPOL aggregates. It does not yet contain authorized intradistrict units, coordinates, census linkage, or municipal context required for the full geospatial objective.

## 2. Research stages

| Stage | Status | Scope |
|---|---|---|
| Public district-level benchmark | Completed | Monthly theft-plus-robbery reports for Comas, January 2018–May 2026. |
| Rapid systematic literature review | Completed with stated limits | OpenAlex and Crossref; 23 empirical studies included. |
| Intradistrict geospatial study | Pending authorization and suitable data | Territory-month modeling, spatial transfer, contextual predictors, and aggregate maps. |
| Institutional pilot or deployment | Not authorized | Requires separate ethics, legal, performance, and governance review. |

## 3. Research questions

### 3.1 Implemented benchmark question

Can lagged, seasonal, trend, and machine-learning models improve next-month prediction of aggregated theft and robbery reports in Comas compared with persistence and seasonal-naive baselines under a final temporal holdout?

### 3.2 Full doctoral question

To what extent can authorized crime history, socioeconomic variables, and geospatial characteristics improve monthly property-crime prediction across safe territorial units in Comas, compared with historical baselines, under temporal and spatial validation?

## 4. Objectives

### 4.1 Completed objectives

1. Acquire and document an official public aggregate dataset with source, license, version, and hash.
2. Construct a complete district-month theft and robbery series for Comas.
3. Engineer leakage-controlled temporal and seasonal predictors.
4. Compare two transparent baselines with four regression models.
5. Evaluate 16 future forecast months and retain unfavorable results.
6. Publish code, tests, forecasts, figures, notebook outputs, model card, and governance documentation.

### 4.2 Pending full-study objectives

1. Obtain lawful access to appropriate intradistrict aggregate units and contextual predictors.
2. Assess data quality, geocoding, spatial support, population exposure, and disclosure risk.
3. Evaluate temporal and grouped spatial transfer.
4. Report calibration or count-forecast uncertainty, interpretability, and territorial error disparities.
5. Determine whether evidence supports an aggregate research prototype; deployment is not presumed.

## 5. Hypotheses and current findings

**H1:** A trained model will outperform persistence on future monthly observations.

**Finding:** Not supported in the implemented benchmark. Persistence achieved MAE 37.19, lower than ridge regression (43.11), random forest (46.99), linear regression (47.11), and histogram gradient boosting (56.14).

**H2:** Recent crime history contains useful next-month predictive information.

**Finding:** Supported at benchmark level because persistence obtained positive test R² of 0.141 and outperformed the 12-month seasonal comparator. This is predictive, not causal, evidence.

**H3:** Contextual and geospatial integration improves transfer across territorial units.

**Finding:** Not tested. The public source has one district-month series and no intradistrict geometry.

## 6. Current data and study population

- **Publisher:** Ministry of the Interior of Peru.
- **Originating system:** SIDPOL.
- **Geographic filter:** Comas UBIGEO `150110`.
- **Source coverage:** January 2018–May 2026.
- **Unit of analysis:** district-month.
- **Outcome:** theft plus robbery reports in the following month.
- **Series:** 101 months and 47,554 reports.
- **Privacy:** public aggregate counts with no personal identifiers or point coordinates.

Future restricted records, linkage keys, exact coordinates, addresses, victims, complainants, or investigated persons must never be stored on GitHub.

## 7. Implemented analysis

1. Preserve the downloaded source and SHA-256 hash.
2. Select Comas by UBIGEO and select theft and robbery categories.
3. Pivot to a complete monthly series.
4. Construct current counts, 1/2/3/6/12-month lags, shifted 3/6-month rolling means, recent trend, time index, and cyclic month terms.
5. Define the following month as the target.
6. Train on feature months before January 2025.
7. Evaluate forecasts from February 2025 through May 2026.
8. Compare persistence, seasonal naive, linear regression, ridge regression, random forest, and histogram gradient boosting.
9. Report MAE, RMSE, R², MAPE, month-level forecasts, and repeated-seed results.

## 8. Bias, ethics, and responsible use

Registered police reports reflect occurrence, reporting behavior, access, classification, and institutional recording practices. The model must not be interpreted as measuring complete crime or inherent territorial danger. The current evidence does not authorize patrol allocation, enforcement, individual profiling, automated decisions, or public risk labeling.

Any future restricted-data study requires a lawful basis, custodian authorization, applicable ethics review, data minimization, access control, disclosure review, and explicit human accountability.

## 9. Reproducibility

The repository versions the source manifest, data dictionary, exact processing code, parameters, seeds, tests, seed-level metrics, model comparison, month-level forecasts, figures, and an executed notebook. Exact reproduction uses the source-file hash recorded in the datasheet and manifest.

## 10. Limitations

The benchmark covers one district and 101 months; it includes pandemic disruption and temporal drift; it lacks monthly exposure and contextual predictors; and it cannot perform intradistrict spatial validation, fairness comparisons, external validation, causal inference, or intervention evaluation.

## 11. TRL statement

No TRL 4 claim is made from the district-level benchmark alone. A technology-readiness claim requires evidence against the applicable CONCYTEC definition, validation of integrated components in the specified environment, documented requirements, and independent verification.

## 12. Amendments

| Date | Amendment | Reason |
|---|---|---|
| 2026-08-09 | Replaced the earlier demonstration phase with an official public district-level SIDPOL benchmark. | A lawful public aggregate source covering Comas became available. |
| 2026-08-09 | Recorded negative model-comparison result. | Persistence outperformed every trained ML model on the final holdout. |
| 2026-08-09 | Separated completed district forecasting from pending intradistrict geospatial validation. | Prevent overstatement of spatial resolution and readiness. |
