# Research Question And Method-Fit Matrix

## 2.1. Refined Research Question

How accurately can a supervised Machine Learning model, enriched with geospatial and socioeconomic features, predict monthly urban crime-risk levels in territorial units of Comas, Lima Metropolitana, and which variables contribute most to the prediction?

## 2.2. Three Candidate Methods

| Method | Short Description |
|---|---|
| **Method 1 - Applied predictive modeling with geospatial feature engineering** | Integrate historical crime complaints, census indicators, territorial segmentation, and temporal variables to train and validate supervised models for risk-level prediction. |
| **Method 2 - Descriptive geospatial hot-spot analysis** | Use maps, kernel density, and clustering to identify historical concentration of incidents without training a forward-looking predictive model. |
| **Method 3 - Qualitative institutional case study** | Interview municipal, police, and community actors to understand preventive-management practices, data use, and adoption barriers. |

## 2.3. E.D.F.C.V. Matrix

| Criterion | What It Asks | Method 1 | Method 2 | Method 3 |
|---|---|---:|---:|---:|
| **E - Epistemological fit** | Does the method match the quantitative applied paradigm? | 5 | 4 | 2 |
| **D - Data availability** | Can lawful data at the required resolution be accessed at this stage? | 4 | 4 | 3 |
| **F - Feasibility** | Can it be demonstrated within the current course artifact? | 5 | 5 | 2 |
| **C - Contribution type** | Does it answer the actual predictive and technological question? | 5 | 3 | 2 |
| **V - Venue fit** | Does it fit AI, smart cities, urban analytics, and public-safety venues? | 5 | 4 | 3 |
| **Total** |  | **24** | **20** | **12** |

The matrix supports Method 1 because the project is explicitly about developing and validating a predictive model, not only describing historical risk or studying institutional perceptions.

## 2.4. Why Method 1 Wins

Method 1 is the strongest fit because it produces the artifact promised by the proposal: a laboratory-validated model for urban crime-risk prediction. It allows the project to compare algorithms, evaluate predictive performance, document a reproducible data pipeline, and generate interpretable risk indicators.

It also matches the expected TRL 4 outcome. A prototype validated in a controlled environment needs engineered data, repeatable experiments, model evaluation, and technical documentation. Descriptive mapping can support the analysis, but it cannot replace model validation.

## 2.5. Why Method 2 Does Not Win

Descriptive geospatial hot-spot analysis is valuable and should be part of the exploratory phase. However, it is mainly retrospective. It can show where incidents were concentrated, but it does not directly estimate future or next-period risk under a defined validation strategy.

For this project, maps are not the final method by themselves. They are an interface and interpretation layer for the predictive workflow.

## 2.6. Why Method 3 Does Not Win

A qualitative institutional case study would be useful for understanding adoption, governance, and responsible-use concerns. It could become a later extension when the prototype is tested with municipal or security actors.

At this stage, however, the core deliverable is technical validation. A qualitative approach alone would not produce the predictive model, metrics, or geospatial risk outputs required by the proposal.

## 2.7. Open Tension

The chosen method is strong for predictive validation but cannot, by itself, prove causal explanations of crime. It also depends on the quality and representativeness of historical complaint data. The protocol should therefore include data-quality checks, temporal validation, bias analysis, and careful language: the model estimates risk patterns, it does not identify offenders or justify automatic policing actions.
