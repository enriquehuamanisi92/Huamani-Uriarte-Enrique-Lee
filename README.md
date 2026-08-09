# Urban Crime Risk Prediction in Comas

**Author:** Enrique Lee Huamani Uriarte

**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies, UNMSM

**Status:** research protocol and completed real-data district-level forecasting experiment

## Project in one paragraph

This research develops and evaluates a machine-learning workflow for next-month property-crime reports in Comas. The completed public-data experiment uses aggregated Ministry of the Interior/SIDPOL records from January 2018 through May 2026, filtered through Comas UBIGEO 150110. It predicts district-level theft-plus-robbery volume and does not identify individuals, predict offenders, or authorize automated policing decisions. Finer territorial modeling remains conditional on access to authorized intradistrict data.

## Research question and general objective

**Current benchmark question:** Can temporal machine-learning models improve next-month forecasting of aggregated theft and robbery reports in Comas over persistence and seasonal-naive baselines under a final future holdout?

**Full doctoral objective:** Extend the official district-level benchmark with authorized contextual and intradistrict data, evaluate temporal and spatial transfer, and implement privacy, fairness, uncertainty, explainability, and human-oversight safeguards.

## Repository map

| Folder | Content |
|---|---|
| `01_paradigm/` | Paradigm, scope, and epistemological position. |
| `02_method/` | Method comparison and consistency matrix. |
| `03_protocol/` | Initial outline and complete protocol v1.0. |
| `04_literature/` | Executed rapid SLR, PRISMA flow, screening records, evidence matrix, and research gaps. |
| `05_pipeline/` | Official public data, completed training pipeline, notebook, forecasts, and technical booklet. |
| `06_repro_audit/` | Reproducibility audit and verification checklist. |
| `07_model_card/` | Model card and dataset datasheet. |
| `08_prociencia/` | PROCIENCIA submission context, evidence status, and expected Peruvian impact. |
| `09_ethics/` | Ethics protocol and use limitations. |
| `10_data_mgmt/` | Research data management plan. |
| `11_bias_audit/` | Bias and subgroup-performance audit plan. |
| `12_integrity/` | AI-use and scientific-integrity policy. |

## Evidence status

- **Completed:** methodological formulation, protocol v1.0, governance documents, rapid SLR, and reproducible real-data district-level forecasting pipeline.
- **Completed with stated scope:** rapid SLR using OpenAlex and Crossref, including preserved exports, record-level screening, 23 empirical studies, and a PRISMA flow.
- **Pending:** institutional-database literature extension; authorized intradistrict/contextual data; geospatial, external, calibration/uncertainty, and territorial-disparity validation; ethics review for any restricted-data phase.

## PROCIENCIA application context

This project was formally submitted to PROCIENCIA call **E041-2026-02, “Applied Research Projects 2026-02,”** under registration number **102632** on February 27, 2026, in the Advanced track for Metropolitan Lima through Asociación Civil Universidad de Ciencias y Humanidades (UCH). Submission does not imply selection or funding. The public-data experiment establishes a district-level forecasting benchmark; progression toward an intradistrict laboratory prototype still requires authorized finer-grained data. See `08_prociencia/prociencia_application.md`.

## Reproducing the real-data experiment

```bash
cd 05_pipeline
py -3 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python src/run_experiments.py
.venv\Scripts\python src/make_figures.py
```

The results describe monthly registered police reports and must not be interpreted as complete crime incidence or causal evidence. See `05_pipeline/README.md` and the completed modeling booklet for scope and limitations.

## Responsible use

Restricted SIDPOL records, addresses, point coordinates, victim data, complainant data, or information about investigated persons must never be uploaded to GitHub. The included source is a licensed public district-month aggregate containing no personal records. Any institutional use requires separate authorization, appropriate ethics review, additional validation, bias auditing, and documented human decision-making.

## Key methodological and regulatory sources

- Congress of the Republic of Peru. Law No. 29733, Personal Data Protection Law.
- CONCYTEC. Directive No. 001-2022-CONCYTEC-P on Technology Readiness Levels.
- Page et al. (2021). PRISMA 2020 statement. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71
