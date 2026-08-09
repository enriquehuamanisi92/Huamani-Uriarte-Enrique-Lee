# Project Presentation Script

## Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in Comas, Metropolitan Lima

**Presenter:** Enrique Lee Huamani Uriarte  
**Estimated duration:** 12–15 minutes  
**Repository:** `Huamani-Uriarte-Enrique-Lee`

## Before starting

Open `START_HERE.md` in the repository. Keep these three links ready in separate browser tabs:

1. `04_literature/systematic_review.md`
2. `05_pipeline/notebook.ipynb`
3. `05_pipeline/docs/modeling_booklet.md`

Do not say that the current model predicts exact locations inside Comas. The completed experiment forecasts monthly registered theft and robbery reports for the whole district. Intradistrict geospatial prediction is the next authorized research stage.

## 1. Opening — about 45 seconds

**Say:**

Good morning. My name is Enrique Lee Huamani Uriarte. Today I will present my doctoral research project, entitled “Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in the District of Comas, Metropolitan Lima.”

The purpose of this project is to examine whether historical police-report data and machine-learning methods can provide reproducible and responsible evidence for preventive urban management. The GitHub repository is not only a collection of documents. It contains the research logic, the literature review, the official dataset, the complete data-processing and model-training workflow, an executed notebook, results, and the corresponding ethical and reproducibility controls.

## 2. Repository map — about 45 seconds

**Show:** `START_HERE.md`

**Say:**

The repository is organized as a research dossier. The numbered folders represent the sequence of the investigation. Folders 01 to 04 establish the scientific and methodological foundation. Folder 05 contains the completed computational experiment. Folders 06 to 12 document reproducibility, responsible use, the PROCIENCIA application, data governance, bias, and scientific integrity.

I will now explain each numbered folder and show the most important evidence.

## 3. Folder 01 — Research paradigm — about 40 seconds

**Open:** `01_paradigm/paradigm_justification.md`

**Say:**

Folder 01 explains the research paradigm. The project mainly follows a post-positivist position because predictions are treated as probabilistic and open to error, replication, and revision. It also has a pragmatic component because the value of the model depends on whether it produces useful evidence under real operational, ethical, and data limitations. The conceptual diagram in this folder is explanatory; it is not presented as empirical evidence.

## 4. Folder 02 — Methodological consistency — about 55 seconds

**Open:** `02_method/consistency_matrix.md`

**Say:**

Folder 02 connects the research problem, objectives, hypotheses, variables, methods, and evidence. It distinguishes two levels. The completed benchmark uses official district-level monthly data. The full doctoral extension will require authorized intradistrict and contextual data for geospatial validation.

The current benchmark asks whether historical monthly information can predict the following month’s registered theft and robbery volume in Comas. This distinction prevents the repository from claiming that a geospatial system has already been validated when the public dataset does not contain coordinates or smaller territorial units.

## 5. Folder 03 — Research protocol — about 55 seconds

**Open:** `03_protocol/protocol_v1.0.md`

**Say:**

Folder 03 contains the research protocol. Version 1.0 defines the study population, unit of analysis, temporal validation, metrics, data sources, ethical restrictions, and current limitations. It also records which activities are completed and which remain pending.

The current unit of analysis is one month in the district of Comas. The outcome is the next month’s combined number of registered theft and robbery reports. The protocol avoids random train-test splitting because random splitting could leak future information into the training stage. Instead, the models are evaluated on a later chronological period.

## 6. Folder 04 — Literature review and PRISMA — about 1 minute 20 seconds

**Open:** `04_literature/systematic_review.md`

**Say:**

Folder 04 contains the rapid systematic literature review prepared according to a documented PRISMA-style workflow. The search identified 100 records, of which 97 were unique. Thirty-eight full records were assessed and 23 empirical studies were included.

The folder contains the search strategy, raw search export, screening log, evidence-extraction table, quality appraisal, synthesis, research-gap analysis, and the completed flow diagram. Therefore, the literature section is traceable: another reviewer can inspect why a study was included or excluded.

The main gaps concern limited validation in the Peruvian and Comas context, inadequate comparison with simple operational baselines, insufficient reporting of calibration and uncertainty, limited reproducibility, and weak treatment of territorial bias and feedback risks. These gaps justify the benchmark and the planned doctoral extension.

## 7. Folder 05 — Real data, processing, training, and results — about 3 minutes

**Open first:** `05_pipeline/notebook.ipynb`  
**Then show:** `05_pipeline/docs/modeling_booklet.md`

**Say:**

Folder 05 is the computational core of the project. It uses an official public MININTER/SIDPOL police-report dataset. The preserved source covers January 2018 through May 2026. The pipeline filters Comas using UBIGEO 150110 and selects theft and robbery records. After aggregation, the Comas series contains 101 monthly periods and 47,554 registered reports.

The notebook is already executed. It contains 28 cells, including 11 code cells, and all 11 code cells have execution results with no errors. It shows the complete workflow: loading the official file, validating the schema, filtering Comas, aggregating reports by month, creating lagged and calendar features, defining the chronological split, training models, evaluating predictions, and generating figures.

After feature construction, 72 observations are used for training and 16 later observations are used for the final test period. The comparison includes two transparent baselines and four fitted machine-learning regressors: persistence, seasonal naive, linear regression, ridge regression, random forest, and histogram gradient boosting.

The best result was obtained by the persistence baseline. Its test metrics were a mean absolute error of 37.19 reports, a root mean squared error of 44.95, an R-squared value of 0.141, and a mean absolute percentage error of 11.05 percent.

This is an important scientific result. The more complex machine-learning models did not outperform the simple persistence baseline on the available district-level series. The project therefore does not exaggerate the value of algorithmic complexity. Instead, it establishes a defensible benchmark and shows that richer, lawfully obtained spatial and contextual predictors must demonstrate genuine incremental value.

The modeling booklet explains every stage in readable form and includes the observed series, model comparison, and test-period forecast figures. The scripts can recreate the result, and automated tests verify the number of months, total reports, chronological ordering, and feature completeness.

## 8. Folder 06 — Reproducibility audit — about 40 seconds

**Open:** `06_repro_audit/reproducibility_audit.md`

**Say:**

Folder 06 audits reproducibility. It records the dataset source, frozen artifact, checksum, software requirements, scripts, outputs, tests, and notebook execution. The purpose is to ensure that the reported values come from executable code and the preserved official dataset rather than manually created tables. The audit also identifies remaining limitations, including dependence on a large source file and the absence of finer-grained public spatial variables.

## 9. Folder 07 — Model Card and Datasheet — about 45 seconds

**Open:** `07_model_card/model_card.md`

**Say:**

Folder 07 contains the Model Card and Datasheet. The Model Card states what was trained, how it was evaluated, its intended research use, and prohibited interpretations. The Datasheet describes the official data source, geographic and temporal coverage, transformations, licensing, and known limitations.

The output must not be interpreted as the true incidence of crime because police reports are affected by reporting behavior, access to institutions, classification practices, and administrative changes. It must also not be used for individual profiling, automated policing, or autonomous resource allocation.

## 10. Folder 08 — PROCIENCIA submission — about 55 seconds

**Open:** `08_prociencia/prociencia_application.md`

**Say:**

Folder 08 documents the PROCIENCIA application. The proposal was formally submitted to call E041-2026-02, Applied Research Projects 2026-02, under registration number 102632 on February 27, 2026, at 12:42:26 Peru time. It was submitted in the Advanced modality for Metropolitan Lima through Universidad de Ciencias y Humanidades.

This statement is supported by the PROCIENCIA-generated application PDF. However, submission does not mean selection or funding. The repository clearly keeps these statuses separate. The official results are scheduled for publication from August 31, 2026.

## 11. Folder 09 — Ethics — about 45 seconds

**Open:** `09_ethics/ethics_protocol.md`

**Say:**

Folder 09 establishes the ethical safeguards. The current experiment uses aggregated public records and does not contain direct personal identifiers. Future use of restricted or finer-grained records will require lawful access, institutional review, secure custody, minimization, safe spatial aggregation, and purpose limitation.

The project adopts a non-punitive and human-supervised approach. Predictions must never be treated as evidence that a person or community is criminal.

## 12. Folder 10 — Data management — about 40 seconds

**Open:** `10_data_mgmt/data_management_plan.md`

**Say:**

Folder 10 is the Data Management Plan. It explains data provenance, storage, formats, access controls, retention, documentation, licensing, backups, and the distinction between public aggregate data and possible future restricted data. This plan supports traceability and the FAIR principles while recognizing that privacy restrictions may limit open publication of sensitive information.

## 13. Folder 11 — Bias audit — about 45 seconds

**Open:** `11_bias_audit/bias_audit_plan.md`

**Say:**

Folder 11 addresses bias and impact. The current dataset permits temporal error analysis but not a valid intradistrict fairness comparison because it lacks smaller spatial units and demographic exposure variables. The project therefore does not invent subgroup results.

Future evaluation will examine reporting bias, geographic coverage, temporal drift, calibration, unequal error distribution, feedback loops, and the risk that forecasts could reinforce existing patterns of enforcement rather than measure underlying harm.

## 14. Folder 12 — Scientific integrity and AI use — about 40 seconds

**Open:** `12_integrity/ai_use_policy.md`

**Say:**

Folder 12 documents scientific integrity and the use of artificial intelligence. AI assistance was used for repository organization, English-language revision, code and documentation support, and locating public sources. The empirical values were produced by executed code from the preserved official dataset; they were not invented by an AI system. The researcher remains responsible for verifying sources, methods, outputs, citations, and the final submission.

## 15. Closing — about 1 minute

**Return to:** `START_HERE.md`

**Say:**

In conclusion, this repository demonstrates a completed and reproducible first research stage. It includes a documented literature review, official public data, a complete data-processing and training pipeline, an executed notebook, comparative evaluation, governance documents, and transparent limitations.

The central empirical finding is that persistence remained stronger than the tested machine-learning models for district-level monthly forecasting. This result is not a failure. It is a scientifically useful benchmark showing that complexity must earn its place through better evidence.

The next stage is to obtain lawful access to finer-grained spatial and contextual data, perform temporal and spatial validation, evaluate uncertainty and bias, and determine whether a responsible geospatial prototype can provide incremental value for preventive management in Comas.

Thank you. I am ready for your questions.

## Likely questions and suggested answers

### Question 1: Is the dataset real?

**Answer:** Yes. The completed experiment uses an official public MININTER/SIDPOL police-report file. For Comas, the pipeline identifies 101 monthly periods and 47,554 registered theft and robbery reports between January 2018 and May 2026.

### Question 2: Where is the model training process?

**Answer:** It is in Folder 05. The executed `notebook.ipynb` shows data loading, validation, filtering, feature engineering, chronological splitting, model fitting, evaluation, forecasts, and figures. The same process is available as reusable Python scripts.

### Question 3: Why did persistence outperform machine learning?

**Answer:** The available public series has only district-level monthly counts and limited predictor diversity. Recent report volume is therefore a strong predictor, while complex models have little additional information from which to learn. This finding motivates, but does not prejudge, the later evaluation of authorized spatial and contextual data.

### Question 4: Does the current model produce crime-risk maps?

**Answer:** Not yet. The official public source used in the benchmark has no intradistrict coordinates or smaller territorial units. Risk mapping belongs to the next research stage and requires authorized data, spatial-quality controls, ethics review, and safe aggregation.

### Question 5: Has PROCIENCIA funded the project?

**Answer:** The project was formally submitted under registration number 102632. Selection and funding have not yet been confirmed. The repository deliberately distinguishes submission from award status.

### Question 6: Why is R-squared relatively low?

**Answer:** Monthly police-report volumes include abrupt changes and factors not represented in the public table. R-squared measures explained variation, so the modest value indicates that the current predictors do not explain all fluctuations. MAE, RMSE, and MAPE are reported alongside R-squared to provide a more complete evaluation.

### Question 7: Can this system be deployed by the police now?

**Answer:** No. This is a research benchmark, not an operational decision system. Deployment would require better data, external validation, governance agreements, bias and impact assessment, security controls, human oversight, and explicit authorization.

### Question 8: What is the original contribution?

**Answer:** The contribution is an auditable Comas-specific benchmark that integrates methodological consistency, literature evidence, real official data, temporal evaluation, reproducibility, and responsible-AI controls. It also preserves a transparent negative result instead of claiming that a complex algorithm is automatically superior.

### Question 9: What would you improve next?

**Answer:** I would obtain lawfully authorized intradistrict data, integrate temporally appropriate population and urban-context variables, test spatial transfer, evaluate calibration and uncertainty, audit territorial disparities, and compare every advanced method against the current persistence benchmark.

### Question 10: How can another researcher reproduce the experiment?

**Answer:** The repository includes the frozen official dataset, requirements, scripts, fixed parameters, model-comparison tables, forecasts, figures, an executed notebook, and automated tests. The commands are documented in the README and modeling booklet.

## Final presentation checklist

- Confirm that GitHub is open and signed in before class.
- Start from `START_HERE.md`, not from the raw file list.
- Show the PRISMA counts in Folder 04.
- Spend the most time on Folder 05 and the executed notebook.
- State the real-data scope: Comas, 101 months, 47,554 reports.
- State the winning result: persistence, MAE 37.19 and MAPE 11.05%.
- Explain that a simple model outperforming complex models is a valid result.
- State “submitted to PROCIENCIA,” not “funded by PROCIENCIA.”
- Clearly distinguish the completed district benchmark from the future geospatial extension.
- Finish by emphasizing reproducibility, ethical safeguards, and the next research stage.
