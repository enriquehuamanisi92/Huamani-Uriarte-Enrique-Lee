# Research Protocol Outline (v0.1)

## 1. Working Title

Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Lima Metropolitana.

## 2. Problem And Context

Comas faces complex urban dynamics related to population density, socioeconomic heterogeneity, commercial activity, mobility corridors, and patrimonial or economic crime risk. Preventive management often relies on retrospective descriptive statistics, which limits the capacity to anticipate territorial and temporal patterns inside the district.

The central problem is the absence of a validated predictive and geospatial model that integrates historical police complaints with socioeconomic and territorial variables to support preventive urban-security management.

## 3. Rationale

The project is justified by the need to move from reactive reporting toward evidence-based anticipation. A predictive model can help identify territorial units and months with higher projected risk, allowing future decision-makers to prioritize prevention, diagnostics, and resource planning.

At the same time, this work must be framed responsibly. The system is a laboratory prototype for decision support, not an automatic enforcement mechanism. Any future deployment must include privacy protection, aggregation, bias auditing, human oversight, and institutional validation.

## 4. General Research Question

How accurately can a Machine Learning and geospatial analysis model predict urban crime-risk levels in Comas using historical complaint records and socioeconomic-territorial variables?

## 5. Specific Questions And Working Hypothesis

The study asks:

- Which territorial, socioeconomic, built-environment, and temporal variables are most associated with projected crime-risk levels?
- Which supervised model provides the best predictive performance under temporal validation?
- How can model outputs be translated into interpretable geospatial risk indicators for preventive management?
- What methodological safeguards are needed to reduce privacy, bias, and misuse risks?

The working hypothesis is that integrating historical police complaint patterns with census and territorial features improves the prediction of urban crime-risk levels compared with purely descriptive or single-source approaches.

## 6. Research Paradigm

The project adopts a quantitative applied technological paradigm. It combines empirical data analysis, supervised learning, geospatial feature engineering, and laboratory validation of a computational artifact.

## 7. Study Design And Data Sources

The intended full study design is an applied predictive-modeling study using repeated territorial-time observations for Comas. The proposed real-world sources are:

- historical police complaint data from SIDPOL for 2018-2025
- socioeconomic and demographic variables from the 2017 National Census
- official district cartography and territorial segmentation
- optional municipal or open-data indicators related to public lighting, commercial density, mobility, CCTV, and patrol coverage

The current repository uses synthetic data that imitates these structures for reproducibility practice only.

## 8. Main Variables

The target variable is a binary or ordinal crime-risk label for the next month or evaluation period at the territorial-unit level.

Candidate predictors include:

- prior incident intensity and recent trend
- crime type composition
- month, quarter, and seasonal indicators
- population density and socioeconomic vulnerability
- commercial density and mobility pressure
- distance to transit corridors or high-flow roads
- public-lighting proxy
- patrol or CCTV coverage proxy
- geospatial coordinates and territorial cell identifiers

## 9. Analysis Plan

The analysis will follow a reproducible workflow:

1. Data integration and cleaning.
2. Territorial-time aggregation.
3. Feature engineering for temporal, socioeconomic, and geospatial predictors.
4. Exploratory mapping and descriptive diagnostics.
5. Model training with algorithms such as logistic regression, Random Forest, Gradient Boosting, Support Vector Machines, and neural networks.
6. Temporal holdout validation and cross-validation.
7. Evaluation through AUC-ROC, PR-AUC, accuracy, F1-score, precision, and recall.
8. Interpretation of variable importance and error patterns.
9. Generation of risk-map-ready outputs.

## 10. Ethics, Limitations, And Timeline

The project must comply with Peruvian personal-data protection rules and scientific-integrity standards. Real complaint records must be anonymized, aggregated, and handled under access control. The model must not expose individual victims, suspects, addresses, or personally identifiable information.

Main limitations include complaint underreporting, spatial reporting bias, temporal instability, incomplete geocoding, and the risk of reinforcing historical inequalities. Mitigation strategies include aggregation, documentation of missingness, temporal validation, bias checks, explainability analysis, and responsible-use guidelines.

The proposed execution period is 24 months, moving from data integration and methodology design to model development, laboratory validation, prototype documentation, scientific publication, and preparation for later TRL 5 validation.
