# Research Consistency Matrix

## Core formulation

| Element | Operational formulation |
|---|---|
| Problem | Preventive management in Comas relies largely on retrospective, fragmented information. No locally validated spatiotemporal model integrates complaints, census attributes, and urban context to estimate next-period risk. |
| General question | To what extent can an integrated model predict monthly property-crime risk by territorial unit, compared with historical baselines, under temporal and spatial validation? |
| General objective | Develop and validate an ML and geospatial model for monthly crime-risk estimation and responsible preventive decision support. |
| General hypothesis | The integrated model will show better out-of-sample discrimination and predictive utility than a crime-history-only baseline, without substantial calibration deterioration across territorial sectors. |
| Proposed unit of analysis | Aggregated territorial unit in Comas by month. The final geometry—grouped census blocks, grid cells, or H3 hexagons—will depend on data quality and disclosure constraints. |
| Study population | Eligible territory-month observations in Comas during 2018-2025 that meet quality, geocoding, and privacy requirements. |

## Objectives, evidence, and analysis

| Specific objective | Variable or evidence | Indicator | Planned analysis |
|---|---|---|---|
| SO1. Build a documented spatiotemporal dataset. | Aggregated complaints, census, and urban context. | Completeness, duplicates, geocoding, temporal consistency. | Profiling, quality rules, and missingness analysis. |
| SO2. Characterize spatial and temporal patterns. | Property-crime count and rate. | Trend, seasonality, global/local Moran statistics. | Time series, maps, and spatial autocorrelation. |
| SO3. Train models and baselines. | Predictors available through month t. | Probability or risk for t+1. | Logistic regression, tree models, and persistence baseline. |
| SO4. Validate generalization. | Out-of-sample predictions. | PR-AUC, ROC-AUC, Brier score, calibration, precision, recall, F1. | Rolling temporal windows and grouped spatial splits. |
| SO5. Examine interpretability and bias. | Errors and explanations by sector. | FNR, FPR, calibration, SHAP/permutation importance. | Stratified analysis with confidence intervals. |
| SO6. Translate results into preventive support. | Aggregated maps and scenarios. | Readability, stability, and supervised utility. | Technical and, if authorized, expert evaluation. |

## Main variables

| Role | Variable | Preliminary definition | Scale/source |
|---|---|---|---|
| Primary outcome | Next-month crime incidence | Count or population-adjusted rate of property-crime complaints at t+1; risk categories are secondary. | Authorized, aggregated SIDPOL data. |
| Temporal predictor | Recent history | 1-, 3-, 6-, and 12-month lags, trend, and seasonality, using no future information. | Derived from complaints. |
| Socioeconomic predictor | Territorial vulnerability | Prespecified index derived from census variables with temporal-validity documentation. | 2017 National Census/INEI. |
| Urban predictor | Exposure and environment | Commercial density, connectivity, lighting, or other available indicators. | Official cartography and records. |
| Stratifier | Territorial sector | Spatial grouping for stability and error-disparity assessment. | Official cartography. |

The final outcome and thresholds will be frozen before examining the test set. A synthetic percentile will not become an institutional risk threshold without empirical justification and authorized stakeholder participation.
