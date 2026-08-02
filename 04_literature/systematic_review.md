# Structured Exploratory Literature Review

## Status and scope

This document is a course-level protocol and exploratory synthesis. **It is not yet a completed systematic review.** Earlier counts—106 records identified and 12 included—are not reported as verifiable results because the repository lacks database exports, search dates, record-level decisions, and assessed texts. A PRISMA flow diagram will be generated only after the search is executed.

## Review question

Which methods, data sources, validation strategies, and safeguards have been used to predict aggregated urban crime risk through machine learning and geospatial analysis, and what evidence exists in Latin American settings comparable to Comas?

## Planned search protocol

| Element | Prespecified decision |
|---|---|
| Databases | Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO; supplementary searches in Google Scholar and official organizations. |
| Period | 2008 through the final search date. |
| Languages | English, Spanish, and Portuguese. |
| Search date | **Pending execution and documentation.** |
| Records | Export RIS/BibTeX/CSV; preserve exact query, date, filters, and database total; deduplicate by DOI, title, and authors. |
| Reporting | PRISMA 2020-informed flow; compliance will not be claimed until its checklist is completed. |

### Conceptual query

```text
("crime prediction" OR "crime risk" OR "predictive policing" OR
 "crime forecasting" OR "urban safety")
AND ("machine learning" OR "statistical learning" OR "deep learning")
AND (geospatial OR spatial OR spatiotemporal OR GIS OR hotspot)
AND (urban OR city OR district OR municipal)
```

The query will be adapted to each database and saved verbatim in `search_log.csv`.

## Eligibility

### Inclusion criteria

- Urban territorial studies of crime risk, incidence, concentration, or forecasting.
- Statistical, ML, or spatiotemporal models with out-of-sample evaluation.
- Sufficient reporting of data, spatial unit, forecast horizon, and metrics.
- Empirical studies, directly relevant methodological reviews, and governance documents.

### Exclusion criteria

- Individual prediction of offending, recidivism, guilt, or personal profiles.
- Studies without empirical evaluation when predictive performance is assessed.
- Inaccessible texts or records lacking minimum information after retrieval attempts.
- Duplicates, abstract-only records, and work outside urban territorial analysis.

Two reviewers are preferable for title/abstract and full-text screening. If the course permits only one reviewer, this limitation will be declared and a sample may be checked by a second person without claiming a review that did not occur.

## Extraction and quality assessment

The following will be recorded: citation/DOI, country, period, source, spatial and temporal units, crime type, outcome, predictors, model, baseline, data split, leakage controls, metrics, calibration, external validation, explainability, fairness, and limitations. Quality will be assessed using prespecified criteria for representativeness, temporality, transparency, comparators, generalization, and risk of bias.

## Exploratory synthesis

Foundational literature indicates that crime concentration and spatiotemporal dependence can support territorial forecasts, but practical value depends on the comparator and validation design. Police records are not neutral measurements: they reflect occurrence, reporting, and institutional practices. Accuracy therefore does not eliminate feedback-loop or unequal-surveillance risks.

Five commitments follow for the Comas study:

1. Compare ML against persistence and historical-hotspot baselines.
2. Separate training, tuning, and testing while preserving temporal order.
3. Measure spatial transfer to unseen territories.
4. Report calibration, uncertainty, and territorial errors, not AUC alone.
5. Treat outputs as aggregated decision support, not automated policing.

## Verified seed references

- Chainey, S., Tompson, L., & Uhlig, S. (2008). The utility of hotspot mapping for predicting spatial patterns of crime. *Security Journal, 21*, 4-28. https://doi.org/10.1057/palgrave.sj.8350066
- Mohler, G. O., et al. (2011). Self-exciting point process modeling of crime. *Journal of the American Statistical Association, 106*(493), 100-108. https://doi.org/10.1198/jasa.2011.ap09546
- Perry, W. L., et al. (2013). *Predictive Policing: The Role of Crime Forecasting in Law Enforcement Operations*. RAND. https://doi.org/10.7249/RR233
- Lum, K., & Isaac, W. (2016). To predict and serve? *Significance, 13*(5), 14-19. https://doi.org/10.1111/j.1740-9713.2016.00960.x
- Meijer, A., & Wessels, M. (2019). Predictive policing: Review of benefits and drawbacks. *International Journal of Public Administration, 42*(12), 1031-1039. https://doi.org/10.1080/01900692.2019.1575664
- Richardson, R., Schultz, J. M., & Crawford, K. (2019). Dirty data, bad predictions. *New York University Law Review Online, 94*, 15-55.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

These are starting references, not the included-study set of a completed review.
