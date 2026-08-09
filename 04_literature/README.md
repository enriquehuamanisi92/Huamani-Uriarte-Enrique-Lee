# 04. Systematic Literature Review

This folder documents the systematic rapid review supporting the doctoral project on machine-learning and geospatial methods for territorial urban-crime risk prediction in Comas, Metropolitan Lima.

## Review question

Which methods, data sources, validation strategies, and safeguards have been used to predict aggregated urban-crime risk through machine learning and geospatial analysis, and what evidence exists in Latin American settings comparable to Comas?

## Contents

| File | Purpose |
|---|---|
| [`systematic_review.md`](systematic_review.md) | Complete English-language review, protocol, synthesis, gaps, and conclusions. |
| [`prisma_2020_flow.md`](prisma_2020_flow.md) | Completed PRISMA 2020 flow, counts, exclusions, and consistency checks. |
| [`prisma_flow_diagram.svg`](prisma_flow_diagram.svg) | Filled PRISMA 2020 flow diagram. |
| [`search_log.csv`](search_log.csv) | Exact query, date, filters, exports, and source status. |
| [`search_results_2026-08-09.csv`](search_results_2026-08-09.csv) | Frozen export of the 100 identified records. |
| [`screening_log.csv`](screening_log.csv) | Record-level screening decisions and exclusion reasons. |
| [`evidence_extraction.csv`](evidence_extraction.csv) | Evidence matrix for the 23 included empirical studies. |
| [`gap_analysis.md`](gap_analysis.md) | Research gaps, required evidence, and project response. |
| [`run_literature_search.ps1`](run_literature_search.ps1) | Reproducible retrieval, deduplication, and initial-screening script. |

## Current evidence status

The reproducible rapid review was executed on August 9, 2026, using OpenAlex and Crossref. It identified 100 records, screened 97 unique records, assessed 38 reports, and included 23 empirical studies.

The export, decisions, evidence matrix, and diagram are versioned in this folder. Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO remain pending as an institutional-access extension. The present results are therefore reported as a reproducible rapid review, not as a universally exhaustive search.

## Main preliminary findings

The included literature indicates that spatial concentration, temporal recurrence, mobility, urban form, and relationships among crime types can contribute predictive information. However, performance depends strongly on the spatial unit, forecast horizon, comparator, and validation design. Several studies emphasize accuracy or F1 while providing limited evidence about calibration, uncertainty, external validity, or territorial fairness.

Police and complaint records are not neutral measurements: they combine occurrence, reporting behavior, and institutional practices. The Comas study must therefore compare machine-learning models with simple baselines, preserve temporal order, assess spatial transfer, report calibration and uncertainty, audit territorial errors, and restrict outputs to aggregated decision support under human oversight.

## Reproducing the search

From PowerShell:

```powershell
cd 04_literature
powershell -ExecutionPolicy Bypass -File .\run_literature_search.ps1
```

The script regenerates the frozen-result and screening files and prints all PRISMA counts.
