# Real-Data Machine-Learning Pipeline for Comas

This folder contains the completed data-preparation, feature-engineering, training, and temporal-evaluation workflow for monthly property-crime reports in Comas, Metropolitan Lima.

## Official data source

The analysis uses the public **Police Reports Dataset, January 2018–May 2026**, published by Peru's Ministry of the Interior through the National Open Data Platform. The records originate from the Police Complaints Information System (SIDPOL), maintained by the Peruvian National Police's Information Technology Directorate.

- Publisher: Ministry of the Interior (MININTER)
- Geographic filter: Comas, Lima, UBIGEO `150110`
- Crime categories: `Hurto` (theft) and `Robo` (robbery)
- Temporal unit: month
- License: Open Data Commons Attribution License
- Source: https://www.datosabiertos.gob.pe/dataset/denuncias-policiales-1

The published file is already aggregated by year, month, department, province, district, crime category, and count. It contains no names, addresses, individual coordinates, or personal identifiers.

## Analytical dataset

The Comas subset contains 101 monthly periods from January 2018 through May 2026. Theft and robbery contribute 47,554 official reports. The target is the total number of theft and robbery reports in the following month.

The official file does not contain intradistrict coordinates. Consequently, this implementation forecasts monthly district-level volume for Comas; it does not claim neighborhood-level or point-level geospatial prediction.

## Completed workflow

1. Download and preserve the official MININTER/SIDPOL publication.
2. Select Comas through UBIGEO `150110`.
3. Restrict the outcome to theft and robbery.
4. Aggregate and complete the monthly time series.
5. Construct seasonal, lagged, rolling-average, and recent-trend features.
6. Train linear regression, ridge regression, random forest, and histogram gradient boosting.
7. Compare every model with persistence and 12-month seasonal-naive baselines.
8. Train on observations before January 2025 and evaluate on the final 16 forecast months.
9. Repeat stochastic models across five seeds.
10. Save results, forecasts, provenance, and the completed modeling booklet.

## Main result

| Model | Mean MAE | Mean RMSE | Mean R² | Mean MAPE |
|---|---:|---:|---:|---:|
| Persistence baseline | **37.19** | **44.95** | **0.141** | **11.05%** |
| Ridge regression | 43.11 | 50.71 | -0.093 | 13.04% |
| Random forest | 46.99 | 56.70 | -0.368 | 15.00% |
| Linear regression | 47.11 | 54.85 | -0.279 | 14.38% |
| Histogram gradient boosting | 56.14 | 68.57 | -0.999 | 17.88% |
| Seasonal naive, 12 months | 143.81 | 167.14 | -10.878 | 41.14% |

The persistence baseline performed best. The current feature set therefore does not justify replacing the simple operational comparator with a more complex machine-learning model.

## Files

- `data/sidpol_police_reports_2018_2026.csv`: official public MININTER/SIDPOL aggregate dataset.
- `src/train.py`: filtering, feature engineering, models, metrics, and temporal split.
- `src/run_experiments.py`: five-seed evaluation and result export.
- `docs/modeling_booklet.md`: presentation-ready account of the completed project.
- `docs/model_comparison.csv`: mean performance by model.
- `docs/test_period_forecasts.csv`: observed and predicted test-period values.
- `docs/real_data_summary.csv`: scope and sample summary.
- `docs/source_manifest.csv`: source URL, license, download date, size, and SHA-256 checksum.
- `notebook.ipynb`: executable walkthrough.

## Reproduction

```powershell
py -3 -m pip install -r requirements.txt
py -3 src/run_experiments.py
```

## Interpretation limits

These are registered police reports, not a complete measure of all crime. Reporting behavior, administrative practices, the COVID-19 period, and temporal drift affect the series. The analysis is predictive rather than causal and must not be used to profile individuals or label communities as inherently dangerous.
