# Bias Audit Plan

## Scope

The synthetic phase tests only the audit procedure. A substantive fairness conclusion requires appropriate real data, context, and institutional and community participation. Equal metrics do not guarantee absence of harm.

## Bias sources

- Unequal complaint and geocoding coverage.
- Changes in crime classification or police presence.
- Territorial variables acting as proxies for protected characteristics.
- Small cells with high uncertainty.
- Threshold choices that distribute false positives and false negatives.
- Drift and feedback after any intervention.

## Prespecified assessment

1. Describe coverage and missingness by sector and time.
2. Compare recorded prevalence and sample sizes.
3. Report PR-AUC, Brier score, calibration, FPR, FNR, precision, and recall by sector with bootstrap intervals.
4. Test sensitivity to spatial unit and threshold.
5. Compare models with and without potentially problematic variables.
6. Inspect importance, extreme errors, and temporal stability.
7. Document who bears the cost of each error type.

Subgroups with insufficient counts will not be compared. Territorial categories will not be presented as inherent characteristics of residents.

## Review and monitoring

No universal disparity tolerance is assumed. Before a pilot, relevant parties must define performance and safety limits. Persistent disparity, poor calibration, or insufficient coverage may require additional data, a different model, greater aggregation, or non-use. Version, coverage, predictor drift, calibration, and errors will be reviewed on a prespecified schedule, with a named person authorized to suspend use.
