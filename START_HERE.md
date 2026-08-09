# Start Here — Main Project Deliverables

This page provides direct access to the completed doctoral-project materials.

## Systematic Literature Review

- [Complete English SLR](04_literature/systematic_review.md)
- [Completed PRISMA 2020 flow](04_literature/prisma_2020_flow.md)
- [PRISMA diagram](04_literature/prisma_flow_diagram.svg)
- [Evidence matrix: 23 included studies](04_literature/evidence_extraction.csv)

## Real-Data Machine-Learning Project

- [Pipeline overview](05_pipeline/README.md)
- [Completed modeling booklet](05_pipeline/docs/modeling_booklet.md)
- [Executable notebook](05_pipeline/notebook.ipynb)
- [Model comparison](05_pipeline/docs/model_comparison.csv)
- [Test-period forecasts](05_pipeline/docs/test_period_forecasts.csv)
- [Official-data summary](05_pipeline/docs/real_data_summary.csv)
- [Data source and SHA-256 manifest](05_pipeline/docs/source_manifest.csv)
- [Official MININTER/SIDPOL dataset](05_pipeline/data/sidpol_police_reports_2018_2026.csv)

## Reproducible Code

- [Data preparation and model training](05_pipeline/src/train.py)
- [Repeated experiment runner](05_pipeline/src/run_experiments.py)
- [Automated pipeline tests](tests/test_real_sidpol_pipeline.py)

## Main empirical result

The official public dataset covers 101 monthly periods for Comas from January 2018 through May 2026. Theft and robbery contribute 47,554 registered reports. Under the final temporal holdout, the persistence baseline achieved the best performance: MAE 37.19, RMSE 44.95, R² 0.141, and MAPE 11.05%.
