# Systematic Literature Review (SLR)

## Machine Learning and Geospatial Analysis for Territorial Urban-Crime Risk Prediction

**Author:** Enrique Lee Huamani Uriarte

**Program:** Doctoral studies

**Application setting:** Comas District, Metropolitan Lima, Peru

**Version:** SLR 1.1 — August 2026

**Reporting guideline:** PRISMA 2020

> **Evidence status.** A reproducible rapid review was executed on August 9, 2026, using OpenAlex and Crossref: 100 records were identified, 97 unique records were screened, 38 reports were assessed, and 23 empirical studies were included. Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO remain pending as an institutional-access extension.

## Abstract

Spatial and temporal concentrations of crime have motivated statistical, geospatial, and machine-learning methods intended to support preventive planning. Their apparent performance, however, depends on data quality, territorial scale, forecast horizon, baseline selection, and validation design. Complaint and police records also reflect reporting behavior and institutional practices in addition to underlying events. This review identifies methods, data sources, validation strategies, performance measures, explainability mechanisms, and ethical safeguards used in aggregated urban-crime prediction, with attention to evidence relevant to Latin America and Comas. A PRISMA 2020-informed rapid review searched OpenAlex and Crossref for publications from 2008 through August 9, 2026. Of 100 records, 23 empirical studies were included. The evidence supports the predictive relevance of crime history, spatial relationships, urban context, and mobility, but reveals limited attention to calibration, uncertainty, external validity, reproducibility, and territorial fairness. The Comas study should compare complex models with prevalence, persistence, and historical-hotspot baselines; preserve temporal order; test spatial transfer; report calibration and uncertainty; and restrict outputs to aggregated decision support under human oversight.

**Keywords:** urban crime; crime forecasting; machine learning; geospatial analysis; territorial risk; smart cities; PRISMA.

## 1. Introduction

Urban crime displays spatial concentration, temporal recurrence, and associations with characteristics of the built and social environment. These patterns make it possible to formulate models that estimate next-period risk for aggregated territorial units. Such estimates may support preventive planning, but they must not be interpreted as predictions of individual behavior, guilt, or causality.

A useful model must do more than achieve a high headline metric. It should improve upon reasonable baselines, generalize to future periods and unseen territories, provide calibrated estimates, and avoid systematically concentrating error or intervention in particular communities. Evidence from settings comparable to Comas is also necessary to justify choices concerning data, spatial granularity, validation, and governance.

This review supports the doctoral project entitled “Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Metropolitan Lima.”

## 2. Objectives and review questions

### 2.1 General objective

To identify, appraise, and synthesize evidence on machine-learning and geospatial methods used to predict aggregated urban-crime risk, considering performance, validation, reproducibility, explainability, bias, and applicability to Comas.

### 2.2 Specific objectives

1. Characterize data sources, crime types, spatial units, temporal units, and forecast horizons.
2. Compare algorithms, feature engineering, and baseline models.
3. Examine temporal, spatial, and external-validation strategies.
4. Identify discrimination, calibration, utility, and uncertainty measures.
5. Analyze transparency, reproducibility, privacy, fairness, and feedback-loop risks.
6. Determine evidence gaps for Peru, Metropolitan Lima, and Comas.

### 2.3 Main review question

Which methods, data sources, validation strategies, and safeguards have been used to predict aggregated urban-crime risk through machine learning and geospatial analysis, and what evidence exists in Latin American settings comparable to Comas?

### 2.4 Secondary questions

- **RQ1:** Which data sources and spatiotemporal scales are used?
- **RQ2:** Which models and baselines are compared?
- **RQ3:** How do studies prevent information leakage and assess future and territorial generalization?
- **RQ4:** Which metrics, calibration methods, and uncertainty estimates are reported?
- **RQ5:** Which explainability, privacy, fairness, and human-oversight measures are included?
- **RQ6:** Which limitations constrain transfer to Comas?

## 3. Methods

### 3.1 Design and reporting standard

This is a systematic rapid review with narrative and tabular synthesis, informed by PRISMA 2020. A meta-analysis was not planned because substantial heterogeneity was expected in outcomes, crime types, spatial units, forecast horizons, and metrics.

### 3.2 Adapted PICOC framework

| Element | Operational definition |
|---|---|
| Population/problem | Crime events or complaints aggregated within urban spaces. |
| Intervention | Statistical prediction, machine learning, deep learning, or spatiotemporal models. |
| Comparison | Prevalence, persistence, historical averages, historical hotspots, or alternative models. |
| Outcomes | Predictive performance, calibration, utility, generalization, explainability, fairness, and reproducibility. |
| Context | Cities, districts, sectors, grids, or other territorial units, with priority for Latin American evidence. |

### 3.3 Information sources and search date

OpenAlex and Crossref were searched on August 9, 2026. The first 50 relevance-ranked records from each source were exported and preserved. Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO are planned for a subsequent institutional-access extension.

### 3.4 Search strategy

The executed search string was:

```text
spatiotemporal crime prediction machine learning urban
```

The date filter was January 1, 2008, through August 9, 2026. Crossref was additionally restricted to journal articles. Exact endpoints, dates, filters, totals, and exports are documented in `search_log.csv` and `run_literature_search.ps1`.

A broader institutional search should adapt the following conceptual query to each database:

```text
("crime prediction" OR "crime forecasting" OR "crime risk" OR
 "predictive policing" OR "urban safety")
AND ("machine learning" OR "deep learning" OR "statistical learning")
AND (geospatial OR spatial OR spatiotemporal OR GIS OR hotspot)
AND (urban OR city OR district OR municipal)
```

### 3.5 Eligibility criteria

Studies were eligible when they: (1) examined prediction or forecasting of aggregated urban crime or crime risk; (2) used statistical prediction, machine learning, deep learning, or spatiotemporal analysis; (3) described an empirical evaluation; (4) provided sufficient information to identify the target or territorial context; and (5) were published between 2008 and the search date.

Studies were excluded when they focused on individual recidivism, guilt, or offender profiling; were unrelated to urban territorial prediction; were secondary reviews without new empirical evidence; lacked verifiable predictive evaluation; or could not be retrieved through available open-access routes.

### 3.6 Selection process

The two exports contained 100 records. Deduplication by DOI or normalized title removed three duplicates. A documented title rule screened the 97 unique records and excluded 49 records outside the conceptual scope. Forty-eight reports were sought, ten could not be retrieved through open access, and 38 were assessed. Fifteen were excluded because they were secondary reviews, had insufficient scope or document quality, or lacked verifiable predictive validation. Twenty-three empirical studies were included.

The rule and record-level decisions are preserved in `run_literature_search.ps1` and `screening_log.csv`. Initial screening was automation-assisted and subsequently checked against the stated eligibility criteria.

### 3.7 Data extraction and quality appraisal

The evidence matrix records citation, country, data source, crime type, spatial unit, target, model, validation, metrics, main findings, and limitations. `NR` means not reported in the accessible metadata or extracted evidence; it does not mean the feature was absent.

Studies were appraised across representativeness, temporal ordering, comparators, validation, metrics, generalization, transparency, and impact/fairness. No single total quality score was used because it could conceal a critical weakness such as information leakage.

## 4. PRISMA 2020 results

![Completed PRISMA 2020 flow diagram](prisma_flow_diagram.svg)

| Stage | n |
|---|---:|
| Records identified | 100 |
| Duplicates removed | 3 |
| Unique records screened | 97 |
| Records excluded by title rule | 49 |
| Reports sought | 48 |
| Reports not retrieved | 10 |
| Reports assessed | 38 |
| Full-text reports excluded | 15 |
| **Empirical studies included** | **23** |

The arithmetic and grouped exclusion reasons are reported in `prisma_2020_flow.md`.

## 5. Evidence synthesis

### 5.1 Data and spatial representation

Most studies rely on historical police or open municipal crime records. Common spatial representations include grids, neighborhoods, communities, and graphs connecting adjacent or functionally related areas. Several studies enrich crime history with social factors, mobile-phone mobility, social-media signals, street imagery, building footprints, or urban topology.

This diversity supports multisource modeling but creates comparability problems. Crime counts, rates, binary hotspots, and multiclass outcomes answer different questions. Results obtained at one grid size or forecast horizon cannot be transferred directly to another setting.

### 5.2 Modeling approaches

The evidence includes conventional classifiers, regression, clustering, stacking ensembles, convolutional neural networks, time-delay networks, LSTM architectures, graph convolutional networks, hypergraph networks, multimodal learning, transfer learning, and agent-based simulation. Recent studies emphasize joint spatial-temporal representation and relationships among crime types.

Complex models may capture nonlinear dependencies, but their incremental value must be assessed against persistence and historical-hotspot baselines. A model that only outperforms another complex algorithm does not establish operational value.

### 5.3 Validation and metrics

The studies commonly report accuracy, precision, recall, F1, or prediction error. Some compare multiple datasets or cities, but explicit spatial transfer, temporal holdout, calibration, and uncertainty are less consistently documented. Perfect or near-perfect classification results warrant special scrutiny for leakage, imbalance, target construction, and random splitting.

For Comas, the primary evaluation should preserve temporal order, hold out a final period, and test grouped spatial transfer to unseen territories. PR-AUC and Brier score should accompany ROC-AUC, precision, recall, F1, calibration curves, and uncertainty intervals.

### 5.4 Mobility and urban context

The included mult-city mobility study reports F1 improvements of approximately 2%–7% when human-mobility flows are added to historical crime features, depending on city and crime type. Other studies indicate that dynamic population denominators, social factors, imagery, and built-form representations may contribute contextual information.

These sources also introduce risks: mobile-device coverage and social-media participation are unequal, imagery may be outdated, and built-environment associations are predictive rather than causal.

### 5.5 Bias, ethics, and governance

Complaint data combine underlying events, willingness and ability to report, and institutional recording practices. Models trained on these records can reproduce unequal observation or enforcement patterns. Few included technical studies provide comprehensive calibration, fairness, feedback-loop, or human-oversight evaluation.

The proposed system must therefore operate only at an aggregated territorial level, exclude individual profiling, communicate uncertainty, document non-use criteria, audit territorial errors, and require human review. Predicted risk must not be treated as proof that a community or person is inherently dangerous.

## 6. Research gaps

1. No included study provides direct validation for Comas, and Peruvian evidence is scarce in the retrieved corpus.
2. Random train-test splits may overestimate performance when time and space are ignored.
3. Simple operational baselines are not consistently reported.
4. Calibration, uncertainty, and decision utility receive less attention than classification metrics.
5. Provenance, temporal availability, and transformation of predictors are often insufficiently documented.
6. Territorial fairness, privacy, and feedback effects are rarely evaluated together.
7. External transfer across cities or institutional systems remains limited.

## 7. Implications for the doctoral study

The review supports eight design commitments:

1. Use an aggregated territory-month unit and never predict individuals.
2. Restrict predictors to information available before the target month.
3. Use expanding temporal windows and preserve a final untouched test period.
4. Conduct grouped spatial validation on unseen territories.
5. Compare with prevalence, persistence, and historical-hotspot baselines.
6. Report calibration, Brier score, PR-AUC, territorial errors, and uncertainty intervals.
7. Audit provenance, underreporting, coverage, leakage, and disparities.
8. Treat outputs as decision support subject to human oversight and ethical review.

## 8. Limitations

This review used two open scholarly sources and their first 50 relevance-ranked results. Ranking may omit relevant work, and ten candidate reports were not retrievable through the available open-access routes. Initial title screening used a documented rule. The evidence matrix includes `NR` where information was not established from accessible material. Database-specific searches through Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO are needed before claiming a fully exhaustive SLR.

## 9. Conclusion

The evidence supports the conceptual feasibility of territorial urban-crime forecasting based on spatial-temporal dependence, mobility, and urban context, but it does not guarantee local utility in Comas. Valid local evidence requires temporal and spatial validation against simple baselines, together with calibration, uncertainty, data-quality assessment, fairness auditing, and governance safeguards. The project contribution should be an auditable test of whether multisource integration improves prediction—not an assumption that a complex algorithm must win.

## Key references

- Hu, T., et al. (2018). Urban crime prediction based on a spatio-temporal Bayesian model. *PLOS ONE, 13*(10), e0206215. https://doi.org/10.1371/journal.pone.0206215
- Kadar, C., et al. (2022). Enhancing short-term crime prediction with human mobility flows and deep learning architectures. *EPJ Data Science, 11*. https://doi.org/10.1140/epjds/s13688-022-00366-2
- Xia, L., et al. (2021). Spatial-temporal sequential hypergraph network for crime prediction with dynamic multiplex relation learning. *IJCAI 2021*, 1631–1637. https://doi.org/10.24963/ijcai.2021/225
- Zhao, X., et al. (2022). Multi-Type Urban Crime Prediction. *AAAI, 36*(4), 4388–4396. https://doi.org/10.1609/aaai.v36i4.20360
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

## Traceability files

- `search_log.csv`: executed queries and source totals.
- `search_results_2026-08-09.csv`: frozen 100-record export.
- `screening_log.csv`: record-level decisions and reasons.
- `evidence_extraction.csv`: 23-study evidence matrix.
- `prisma_2020_flow.md`: PRISMA counts and arithmetic.
- `run_literature_search.ps1`: reproducible search and screening logic.
