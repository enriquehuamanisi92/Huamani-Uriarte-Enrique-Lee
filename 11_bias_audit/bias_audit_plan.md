# Bias and Impact Audit Plan

## Current scope

The completed experiment uses one aggregate monthly series for Comas. It can assess temporal error and drift but cannot compare intradistrict groups or establish territorial fairness. Equal district-level performance would not demonstrate absence of harm.

## Measurement and modeling risks

- Unequal access or willingness to report crime.
- Changes in police classification and recording practices.
- Pandemic disruption and later temporal drift.
- Category aggregation that may hide offense-specific behavior.
- Small sample size relative to model flexibility.
- False confidence from algorithmic complexity.
- Territorial stigma if district forecasts are treated as inherent community traits.
- Feedback effects if predictions later influence observation or enforcement.

## Current audit

1. Preserve temporal order and use a final future holdout.
2. Compare trained models with persistence and seasonal baselines.
3. Report MAE, RMSE, R², and MAPE without suppressing unfavorable results.
4. Inspect month-level errors during changing series levels.
5. Reject a complex model when it does not improve the simple comparator.
6. State that the outcome measures registered reports, not complete crime incidence.

The current audit found that persistence outperformed every trained model. This is a safety-relevant result: complexity is not justified by the available evidence.

## Requirements for a future territorial audit

If authorized intradistrict units become available, the project must assess coverage, missingness, report volume, calibration, false-positive and false-negative rates, uncertainty, and error by prespecified territorial group. Comparisons require adequate sample sizes and must not treat territorial categories as characteristics of residents.

Sensitivity analyses should vary spatial unit, forecast horizon, outcome definition, threshold, time window, and potentially problematic predictors. Any persistent disparity, poor calibration, weak coverage, or unstable transfer may require greater aggregation, a different model, additional data, or non-use.

## Monitoring and stopping rules

No operational pilot is authorized. Before any future pilot, responsible institutions and affected stakeholders must define acceptable performance, safety limits, human-review responsibilities, correction mechanisms, monitoring frequency, and the authority to suspend or withdraw the system.
