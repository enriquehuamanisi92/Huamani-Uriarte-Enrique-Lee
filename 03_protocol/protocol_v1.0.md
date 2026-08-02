# Research Protocol v1.0

**Title:** Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Metropolitan Lima

**Version:** 1.0 — August 2026

**Author:** Enrique Lee Huamani Uriarte

## 1. Problem statement

Police complaints, census indicators, and urban-environment data describe complementary dimensions of crime risk, but they are usually fragmented and have different spatial and temporal resolutions. Reliance on retrospective reporting limits anticipatory assessment of territorial concentrations. The scientific and technological problem is the absence of a locally validated, reproducible, and responsible model that estimates next-period risk without equating recorded complaints with total crime or interpreting predictive associations as causal explanations.

The study is limited to territorially aggregated property crime. It will not predict individuals, recidivism, guilt, or personal behavior. The exact spatial unit will be selected after assessing coverage, geocoding error, and re-identification risk.

## 2. Rationale

- **Scientific:** assess whether spatiotemporal integration improves generalization over simple baselines.
- **Technological:** produce a versioned pipeline and laboratory-validated prototype, subject to the applicable TRL assessment.
- **Practical:** generate aggregated estimates that may support preventive planning under human oversight.
- **Social and ethical:** incorporate use limitations, privacy, disparity auditing, and uncertainty communication by design.

## 3. Questions, objectives, and hypotheses

### 3.1 General research question

To what extent can a model integrating crime history, socioeconomic variables, and geospatial characteristics predict monthly property-crime risk by territorial unit in Comas, compared with historical baselines, under temporal and spatial validation?

### 3.2 General objective

Develop and validate the integrated model, evaluate discrimination, calibration, utility, and territorial stability, and document safeguards required for preventive decision support.

### 3.3 Specific objectives

1. Integrate and document a territory-month dataset with quality controls and provenance.
2. Describe distribution, trend, seasonality, and spatial autocorrelation.
3. Compare supervised models with prevalence and historical-persistence baselines.
4. Evaluate generalization using rolling temporal windows and spatial splits.
5. Analyze calibration, errors, interpretability, and territorial disparities.
6. Produce aggregated maps, a model card, and a responsible-use protocol.

### 3.4 Hypotheses

**H1:** The integrated model will outperform the historical baseline on PR-AUC and Brier score in future periods.

**H2:** Recent crime-history variables will add predictive information beyond static territorial variables.

**H3:** Performance and calibration will vary across sectors; these differences must be quantified before any institutional use is considered.

H1 and H2 are predictive, not causal, hypotheses. H3 is a heterogeneity hypothesis and safety criterion.

## 4. Design

This is a quantitative applied study for predictive-model development and validation using repeated territory-month observations. The proposed period is 2018-2025, conditional on authorization and data quality. The current phase is a synthetic proof of concept. The real-data phase will be retrospective and non-interventional.

## 5. Population, unit, and eligibility

- **Target population:** territorial units in Comas observed monthly.
- **Unit of analysis:** territory-month.
- **Inclusion:** property-crime complaints within Comas with valid dates, harmonizable classification, and geocoding compatible with safe aggregation.
- **Exclusion:** confirmed duplicates, records outside the scope or period, impossible coordinates, and observations that cannot be aggregated safely.
- **Sample:** census of eligible records. Counts of records, territories, months, and events will be reported after authorization; no sample size is fabricated in advance.

Data sufficiency will be assessed using event counts, prevalence, model complexity, and desired precision of performance estimates. If data are insufficient, model complexity will be reduced or the aggregation unit enlarged.

## 6. Data sources and governance

1. Authorized SIDPOL records, pseudonymized before analytical access.
2. INEI 2017 National Census data, explicitly documenting temporal mismatch.
3. Official cartography and, only when licensing and quality permit, municipal infrastructure variables.

Personal data will never be stored on GitHub. Linkage will occur in a controlled environment; the public repository will contain code, metadata, schemas, and synthetic data only.

## 7. Outcome and predictors

The primary outcome will be the next-month count or population-adjusted rate of property-crime complaints. Secondary analyses may define risk levels using prespecified, justified thresholds. Every predictor must be available by the end of month t. Lags will be calculated within territorial units and audited for information leakage.

## 8. Analysis plan

1. Freeze the data dictionary, eligibility rules, and analysis plan.
2. Assess duplicates, missingness, consistency, coverage, and geocoding error.
3. Describe rates, trends, seasonality, and spatial autocorrelation using global and local Moran statistics where appropriate.
4. Train prevalence and persistence baselines, regularized logistic regression, and tree-based models. More complex models will be used only when sample size and incremental value justify them.
5. Use expanding-window temporal validation and preserve the final period as an untouched test set.
6. Use grouped spatial validation to assess transfer to unseen territories.
7. Tune hyperparameters and decision thresholds using training/validation data only.
8. Report PR-AUC as the main discrimination metric under class imbalance, together with ROC-AUC, precision, recall, F1, Brier score, calibration curves, and bootstrap confidence intervals.
9. Compare models on identical splits and report uncertainty rather than only the best point estimate.
10. Examine permutation importance or SHAP values, temporal stability, and sector-specific errors.

## 9. Bias control

Complaint data reflect victimization, willingness and ability to report, and institutional practices. They will not be treated as a complete measure of crime. Administrative changes, missingness, coverage, and possible feedback loops will be documented. Sensitive personal variables and unjustified proxies will not be used. Territorial comparisons will include sample sizes and uncertainty and will not label communities as inherently dangerous.

## 10. Ethics and data protection

Institutional authorization and applicable ethics review will be required before real data are used. Processing will comply with Peruvian Law No. 29733 and regulations in force at execution. Safeguards include minimization, role-based access, encryption, access logging, aggregation, a deletion schedule, and an incident-response procedure. Public outputs will undergo disclosure review and will not display individual points.

## 11. Reproducibility

Code, parameters, seeds, versions, hashes, and analytical decisions will be versioned. DVC will manage non-sensitive artifacts; MLflow will record experiments without real data or revealing paths. An independent clean-clone reproduction must generate the principal tables before study closure.

## 12. Limitations

Expected limitations include underreporting, reporting bias, classification changes, census time mismatch, spatial dependence, temporal drift, geocoding quality, and limited transportability beyond Comas. A predictive design cannot identify causes or demonstrate that an intervention reduces crime.

## 13. Outputs and TRL progression criteria

- Controlled, documented analytical dataset.
- Reproducible pipeline and automated tests.
- Temporal-spatial validation report.
- Model card, datasheet, bias audit, and ethics protocol.
- Laboratory prototype of an aggregated risk map.

TRL 4 remains a target and will be claimed only when there is verifiable evidence that components were validated in the environment defined by the applicable CONCYTEC directive.

## 14. Summary timeline (24 months)

| Phase | Months | Output |
|---|---:|---|
| Authorization, review, and protocol | 1-4 | Frozen protocol and permissions. |
| Data integration and quality | 5-8 | Audited dataset and dictionary. |
| Analysis and development | 9-14 | Baselines and candidate models. |
| Validation and audits | 15-18 | Temporal, spatial, and bias reports. |
| Prototype and evaluation | 19-21 | Aggregated map and model card. |
| Writing and transfer | 22-24 | Thesis, article, and reproducible package. |

## 15. Amendments

Every change after protocol freezing will record its date, rationale, impact, and whether it occurred before or after test-set inspection. Non-prespecified analyses will be labeled exploratory.
