# UNMSM Research Methods - Enrique Lee Huamani Uriarte

Course repository for *Research Methods and Scientific Integrity in AI and Advanced Technologies* at UNMSM.

**Author:** Enrique Lee Huamani Uriarte  
**Current research topic:** Development and validation of an urban crime risk prediction model based on Machine Learning and geospatial analysis for preventive management in the district of Comas, Lima Metropolitana.

## What This Repository Covers

This repository is organized as a coherent research-methods submission for the first course sessions. It has been restructured around an applied technology project: a laboratory-validated predictive model for urban crime risk in Comas.

The research logic moves from paradigm selection, to method justification, to a first protocol outline, to a literature and gap analysis, and finally to a reproducible technical artifact. The technical artifact uses a synthetic, SIDPOL-like and census-like dataset only for reproducibility practice.

## Current Structure

- `01_paradigm/` - paradigm justification for the applied urban crime risk project
- `02_method/` - research question refinement and method-fit matrix
- `03_protocol/` - protocol outline v0.1
- `04_literature/` - mini literature review, PRISMA-style diagram, and gap analysis
- `05_pipeline/` - reproducible baseline pipeline using synthetic geospatial crime-risk data, DVC, MLflow, and Docker

## How To Read The Project

For the research logic, start with `01_paradigm/` and continue in order to `04_literature/`. These folders define the conceptual and methodological foundation of the project.

For the technical artifact, go directly to `05_pipeline/README.md`. That folder demonstrates how the future analytical workflow could be versioned, trained, evaluated, and tracked in a reproducible way.

## Quick Access

- Research deliverables: `01_paradigm/` to `04_literature/`
- Technical artifact: `05_pipeline/`
- Colab notebook: `05_pipeline/notebook.ipynb`
- Synthetic dataset: `05_pipeline/data/comas_urban_crime_synthetic.csv`
- Saved experiment summary: `05_pipeline/docs/experiment_results.csv`

## How To Reproduce The Current Technical Artifact

The easiest path is Google Colab:

1. Open `05_pipeline/notebook.ipynb` from GitHub or through the Colab link inside `05_pipeline/README.md`.
2. Run the notebook from top to bottom.
3. Use the executed notebook, the saved CSV summary, and the generated `mlruns/` folder as technical evidence for the reproducibility workflow.

If you prefer local execution, the exact steps are documented in `05_pipeline/README.md`.

## Technical Status

The current pipeline uses a small synthetic dataset that imitates the structure of a possible integrated urban crime-risk dataset for Comas. It includes fictional territorial cells, month-level observations, simulated incident pressure, socioeconomic indicators, built-environment proxies, and geospatial coordinates.

It does **not** contain real SIDPOL records, real victim information, real police reports, or operational municipal data. It must not be used to make policing or resource-allocation decisions. Its only purpose is to demonstrate a reproducible prototype workflow aligned with the proposed applied research.

## Project Direction

The full research proposal aims to integrate historical police complaint data from SIDPOL for 2018-2025, socioeconomic and demographic variables from the 2017 National Census, and official urban cartography for Comas. The expected result is a TRL 4 laboratory prototype able to estimate territorial crime-risk levels, support risk maps, and provide a basis for later validation in relevant institutional environments.

## What Is Still Pending For A Full Applied Research Repository

- access-controlled handling of real SIDPOL or institutional datasets
- formal geospatial preprocessing with official Comas territorial units
- final DVC remote setup with an institutional or shared storage location
- data dictionary, metadata, and FAIR-oriented research data management files
- bias, fairness, privacy, and responsible-use audit documentation
- prototype visualization dashboard for projected urban risk maps
- final protocol versions (`v1.0` and `v2.0`)

## Current Completion Status

For the current course scope, the repository includes:

- paradigm justification
- method-fit matrix
- protocol outline v0.1
- mini literature review with a PRISMA-style diagram and gap analysis
- reproducible synthetic baseline pipeline with notebook, DVC pointer, MLflow outputs, and experiment summary

## Integrity Note

The methodological documents are working academic drafts. The technical artifact uses synthetic data and is not a deployed public-safety system. Before any real-world validation, the project must implement privacy safeguards, aggregation rules, bias checks, institutional authorization, and responsible-use restrictions.
