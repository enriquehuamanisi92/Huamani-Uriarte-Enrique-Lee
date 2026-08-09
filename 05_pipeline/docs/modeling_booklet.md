# Completed Machine-Learning Project Booklet

## Monthly Property-Crime Forecasting in Comas, Metropolitan Lima

**Researcher:** Enrique Lee Huamani Uriarte

**Data source:** Ministry of the Interior / SIDPOL

**Study period:** January 2018–May 2026
**Geographic scope:** Comas District, UBIGEO 150110

## Executive summary

This project prepared and evaluated a reproducible forecasting pipeline using official public police-report data for Comas. The study focused on theft and robbery, aggregated monthly, and predicted the next month's combined report volume. Six approaches were evaluated under a temporal holdout: two transparent baselines and four machine-learning regressors.

The persistence baseline achieved the best test performance (MAE 37.19; RMSE 44.95; R² 0.141; MAPE 11.05%). Ridge regression was the strongest trained model but did not outperform persistence. The correct conclusion is therefore that the tested machine-learning models do not yet provide sufficient incremental predictive value over the most recent observed month.

## 1. Research objective

To determine whether machine-learning models using lagged, seasonal, and trend features can improve next-month prediction of aggregated theft and robbery reports in Comas compared with simple historical baselines.

## 2. Provenance and licensing

The source is the *Police Reports Dataset, January 2018–May 2026*, published by Peru's Ministry of the Interior on the National Open Data Platform. It originates from SIDPOL and is distributed under the Open Data Commons Attribution License.

The downloaded table is aggregated and contains: year, month, department, province, district, UBIGEO, crime category, and count. No personal information is used.

## 3. Scope and descriptive results

- National source rows: preserved in the official CSV.
- Comas source rows across all categories: 698.
- Monthly periods for Comas: 101.
- All-category reports in Comas: 144,736.
- Theft reports: 22,934.
- Robbery reports: 24,620.
- Property-crime outcome total: 47,554.
- Average theft-plus-robbery reports per month: 470.83.

Violence against women and family members, extortion, fraud, kidnapping, and the ambiguous “Other” group were not combined with the property-crime outcome.

## 4. Data preparation

The workflow filters Comas through UBIGEO `150110`, pivots theft and robbery into separate monthly columns, and creates a complete monthly index. The response variable is shifted one month forward so that each row uses information available by month *t* to predict reports in month *t + 1*.

## 5. Feature engineering

The final feature set contains:

- current theft, robbery, and combined property-crime reports;
- one-, two-, three-, six-, and twelve-month lags;
- three- and six-month rolling means using past values only;
- recent change between one- and three-month lags;
- linear time index;
- sine and cosine encoding of month-of-year seasonality.

All rolling features are shifted before calculation to avoid future-information leakage.

## 6. Validation design

Observations before January 2025 form the training set. Months from January 2025 onward form the test feature period, predicting February 2025 through May 2026. The temporal order is never shuffled. Random forest was repeated with seeds 13, 21, 42, 87, and 100; deterministic models remain identical across seeds.

## 7. Models

1. Persistence: next month equals the current month.
2. Seasonal naive: next month equals the value from 12 months earlier.
3. Linear regression with standardized features.
4. Ridge regression with standardized features and L2 regularization.
5. Random forest regression.
6. Histogram gradient-boosting regression.

## 8. Results

| Rank | Model | MAE | RMSE | R² | MAPE |
|---:|---|---:|---:|---:|---:|
| 1 | Persistence baseline | **37.19** | **44.95** | **0.141** | **11.05%** |
| 2 | Ridge regression | 43.11 | 50.71 | -0.093 | 13.04% |
| 3 | Random forest | 46.99 | 56.70 | -0.368 | 15.00% |
| 4 | Linear regression | 47.11 | 54.85 | -0.279 | 14.38% |
| 5 | Histogram gradient boosting | 56.14 | 68.57 | -0.999 | 17.88% |
| 6 | Seasonal naive | 143.81 | 167.14 | -10.878 | 41.14% |

Negative R² values indicate that those models performed worse than predicting the test-set mean. The seasonal baseline failed because the series underwent substantial level changes, particularly around and after the pandemic period.

## 9. Interpretation

Recent report volume is more useful than the tested nonlinear models for this district-level monthly series. With only 101 periods and a structural disruption around 2020, flexible models can overfit historical patterns that do not persist into 2025–2026.

This finding supports a cautious operational recommendation: retain persistence as the benchmark and do not claim that machine learning currently improves forecasting. Future gains require additional predictors with known availability before the forecast date, longer post-disruption history, or finer authorized spatial units.

## 10. Limitations

- Police reports reflect events, reporting, and recording practices.
- The public dataset provides district-level aggregates, not intradistrict coordinates.
- The time series is small for high-capacity machine learning.
- COVID-19 and subsequent administrative or behavioral changes create temporal drift.
- Population exposure and socioeconomic predictors were not available in the same monthly official table.
- The analysis forecasts reports and does not identify causes or intervention effects.

## 11. Reproducibility

Run `py -3 src/run_experiments.py` from `05_pipeline`. The command recreates the experiment table, model comparison, real-data summary, and test-period forecasts. Source code, frozen official data, parameters, seeds, and outputs are versioned together.

## 12. Final conclusion

The completed real-data experiment demonstrates a valid machine-learning workflow but does not support deployment of a complex model. The simple persistence baseline remains the strongest tested approach. This transparent negative result is scientifically useful because it prevents overclaiming and establishes a defensible benchmark for future work with richer authorized data.
