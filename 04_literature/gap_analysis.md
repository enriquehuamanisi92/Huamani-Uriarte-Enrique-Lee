# Preliminary Research Gap Analysis

These gaps are propositions that the systematic search must confirm, refine, or reject. They are not presented as final findings.

| Candidate gap | Evidence required | Project response |
|---|---|---|
| Limited published validation at the intra-district scale in Comas. | Reproducible regional search and consultation of Peruvian repositories. | Local study using territory-month observations. |
| Frequent use of random evaluation that ignores time or space. | Extract each study's split and forecast horizon. | Rolling temporal and grouped spatial validation. |
| Insufficient comparison with operationally simple baselines. | Record every included study's comparator. | Prevalence, persistence, and historical-hotspot baselines. |
| Limited integration of complaints, census data, and urban context. | Document sources and granularities used in prior work. | Multi-source pipeline with provenance and sensitivity analysis. |
| Reporting focused on discrimination rather than calibration and utility. | Extract metrics, calibration, and uncertainty estimates. | PR-AUC, Brier score, calibration curves, errors, and intervals. |
| Superficial treatment of bias and feedback risks. | Assess fairness, governance, and intended-use reporting. | Territorial audit, model card, oversight, and non-use criteria. |
| Limited reproducibility of data transformations. | Verify available code, data, parameters, and versions. | Scripts, DVC, curated MLflow summaries, hashes, and clean-clone testing. |

## Proposed contribution

The contribution is not a claim that a complex algorithm must outperform existing methods. It is an auditable evaluation of whether spatiotemporal integration improves prediction and calibration over baselines in Comas under explicit privacy and use constraints. A null result or a superior simple model would also be valuable evidence.

## Confirmation criterion

A gap will enter the final introduction only when supported by the completed evidence matrix. The final claim will state the databases, dates, number of studies, scope, and limitations and will avoid universal generalizations.
