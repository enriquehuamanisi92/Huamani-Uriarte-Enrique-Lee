# Research Gap Analysis After the Rapid Systematic Review

These gaps are supported by the completed rapid systematic review of 23 included studies. Because the review used a bounded rapid-search protocol, the claims should be confirmed or refined through the planned institutional database extension before they are presented as exhaustive findings.

| Candidate gap | Evidence required | Project response |
|---|---|---|
| Limited published validation at the intra-district scale in Comas. | Reproducible regional search and consultation of Peruvian repositories. | Local study using territory-month observations. |
| Frequent use of random evaluation that ignores time or space. | Extract each study's split and forecast horizon. | Rolling temporal and grouped spatial validation. |
| Insufficient comparison with operationally simple baselines. | Record every included study's comparator. | Prevalence, persistence, and historical-hotspot baselines. |
| Limited integration of complaints, census data, and urban context. | Document sources and granularities used in prior work. | Multi-source pipeline with provenance and sensitivity analysis. |
| Reporting focused on discrimination rather than calibration and utility. | Extract metrics, calibration, and uncertainty estimates. | PR-AUC, Brier score, calibration curves, errors, and intervals. |
| Superficial treatment of bias and feedback risks. | Assess fairness, governance, and intended-use reporting. | Territorial audit, model card, oversight, and non-use criteria. |
| Limited reproducibility of data transformations. | Verify available code, data, parameters, and versions. | Versioned scripts, a frozen source manifest and hash, automated tests, an executed notebook, saved forecasts, and clean-run verification. |

## Proposed contribution

The current contribution is an auditable district-level forecasting benchmark using official public records. Its result—that persistence outperformed the tested machine-learning models—is itself useful evidence against assuming that greater model complexity guarantees better forecasts. The full doctoral contribution will test whether legally obtained, finer-grained spatial and contextual variables improve prediction, calibration, and operational usefulness under explicit privacy and use constraints.

## Confirmation criterion

A gap will enter the final dissertation introduction only when supported by the evidence matrix and, where feasible, the institutional database extension. The final claim will state the databases, search dates, number of studies, scope, and limitations and will avoid universal generalizations.
