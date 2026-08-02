# Model Card — Synthetic Prototype

## Identification

- **Name:** Comas Urban Crime Risk Prototype.
- **Version:** 0.1-synthetic.
- **Owner:** Enrique Lee Huamani Uriarte.
- **Status:** proof of concept; not deployable.

## Intended purpose

Demonstrate a reproducible pipeline for estimating aggregated next-month risk by territorial unit. In an authorized future phase, it may support preventive analysis under human oversight.

## Prohibited uses

- Identifying, scoring, monitoring, or detaining individuals.
- Inferring guilt, recidivism, or group membership.
- Automatically allocating patrols, sanctions, or resources.
- Publishing addresses, point coordinates, or re-identifiable maps.
- Presenting synthetic metrics as evidence of real-world effectiveness.

## Current data and outcome

Fully synthetic monthly data for 64 zones from 2018 through 2025. The binary label indicates whether a synthetic next-month count exceeds a global percentile. This teaching definition is not an institutional definition of risk.

## Current evaluation

Saved experiments report ROC-AUC, PR-AUC, accuracy, precision, recall, and F1 on a temporal holdout beginning in 2024. Random Forest reaches approximately 0.84 ROC-AUC. This is expected because the data and outcome follow programmed relationships. Calibration, persistence baselines, intervals, rolling validation, and spatial validation remain pending.

## Risks and release requirements

Risks include underreporting, reporting bias, police feedback, drift, uneven geocoding, territorial stigma, sensitive proxies, and false confidence. Before any status change, the project requires permissions, ethics review, aggregated data, independent testing, baselines, calibration, disparity auditing, uncertainty documentation, human approval, monitoring, and a withdrawal procedure. Current status: **NOT SUITABLE FOR OPERATIONAL USE**.
