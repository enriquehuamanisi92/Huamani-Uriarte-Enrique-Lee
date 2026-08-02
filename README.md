# Urban Crime Risk Prediction in Comas

**Author:** Enrique Lee Huamani Uriarte

**Course:** Research Methods and Scientific Integrity in AI and Advanced Technologies, UNMSM

**Status:** research protocol and proof of concept using synthetic data

## Project in one paragraph

This research proposes developing and validating a machine-learning and geospatial-analysis model that estimates next-month property-crime risk for territorial units in Comas. The study will integrate authorized police complaint records, census variables, and territorial characteristics. Its expected product is a TRL 4 prototype for preventive-management decision support; it does not identify individuals, predict offenders, or authorize automated policing decisions. The current pipeline uses synthetic data exclusively and demonstrates computational reproducibility, not effectiveness under real-world conditions.

## Research question and general objective

**Question:** To what extent can a machine-learning model integrating crime history, socioeconomic variables, and geospatial characteristics predict monthly property-crime risk across territorial units in Comas, compared with historical baselines, under temporal and spatial validation?

**Objective:** To develop and validate this model; evaluate its discrimination, calibration, utility, and territorial stability; and implement privacy, fairness, explainability, and human-oversight safeguards.

## Repository map

| Folder | Content |
|---|---|
| `01_paradigm/` | Paradigm, scope, and epistemological position. |
| `02_method/` | Method comparison and consistency matrix. |
| `03_protocol/` | Initial outline and complete protocol v1.0. |
| `04_literature/` | Exploratory review, search protocol, and research gaps. |
| `05_pipeline/` | Synthetic data, code, notebook, and technical results. |
| `06_repro_audit/` | Reproducibility audit and verification checklist. |
| `07_model_card/` | Model card and dataset datasheet. |
| `09_ethics/` | Ethics protocol and use limitations. |
| `10_data_mgmt/` | Research data management plan. |
| `11_bias_audit/` | Bias and subgroup-performance audit plan. |
| `12_integrity/` | AI-use and scientific-integrity policy. |

## Evidence status

- **Completed:** methodological formulation, protocol v1.0, governance documents, and reproducible synthetic pipeline.
- **Preliminary:** exploratory literature review. Previous PRISMA counts must not be treated as final results until searches and exports are completed.
- **Pending:** authorization and access to real data, geocoding protocol, ethics review, auditable systematic search, and external validation.

## Reproducing the proof of concept

```bash
cd 05_pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python data/create_dataset.py
python src/run_experiments.py
```

Synthetic results must not be cited as evidence about public safety in Comas. See `05_pipeline/README.md` for local, Docker, and Colab instructions.

## Responsible use

SIDPOL records, addresses, point coordinates, victim data, complainant data, or information about investigated persons must never be uploaded to GitHub. Public outputs will be aggregated and subjected to disclosure control. Any institutional use will require authorization, ethics review, validation with real data, bias auditing, and documented human decision-making.

## Key methodological and regulatory sources

- Congress of the Republic of Peru. Law No. 29733, Personal Data Protection Law.
- CONCYTEC. Directive No. 001-2022-CONCYTEC-P on Technology Readiness Levels.
- Page et al. (2021). PRISMA 2020 statement. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71
