# PROCIENCIA Application and Expected Peruvian Impact

## 1. Institutional context

PROCIENCIA is Peru's *Programa Nacional de Investigación Científica y Estudios Avanzados*, operating within the national science, technology, and innovation system under CONCYTEC. It manages resources for scientific research, technological innovation, advanced human capital, and knowledge transfer.

Official sources:

- https://prociencia.gob.pe/nosotros/
- https://www.gob.pe/prociencia
- https://www.gob.pe/14464-que-hacemos-concursos-convocados-por-prociencia

## 2. Application status

The project titled **“Development and Validation of an Urban Crime Risk Prediction Model Based on Machine Learning and Geospatial Analysis for Preventive Management in the District of Comas, Metropolitan Lima”** was submitted to the **Applied Research Projects 2026-02** call.

| Field | Recorded information |
|---|---|
| Applicant institution | Asociación Civil Universidad de Ciencias y Humanidades (UCH) |
| Researcher | Enrique Lee Huamani Uriarte |
| Application identifier shown | 102632 |
| Modality shown | Advanced (*Avanzado*) |
| Thematic area shown | Information and Communication Technologies |
| Public evidentiary claim | Submitted/registered only |

Submission does not imply eligibility, selection, award, funding, or authorization to deploy a public-safety system. Any status change must be supported by an official PROCIENCIA publication or formal institutional communication.

## 3. Current research evidence

Since submission, the repository has completed:

- a reproducible rapid SLR with 100 identified records and 23 included empirical studies;
- an official public-data benchmark using MININTER/SIDPOL district-month aggregates for Comas;
- a 101-month theft and robbery series totaling 47,554 registered reports;
- temporal comparison of two baselines and four fitted regression models;
- an executed notebook, forecasts, figures, model card, datasheet, tests, and reproducibility audit.

The benchmark found that persistence outperformed all trained machine-learning models. This negative result is retained because a technological project must demonstrate incremental value rather than presume it.

## 4. Evidence still required for the proposed geospatial prototype

The public source contains district-month counts but no intradistrict units, coordinates, population exposure, census linkage, or municipal context. The following therefore remain pending:

1. lawful access to appropriate authorized data;
2. ethics and data-governance review for restricted records;
3. safe spatial aggregation and geocoding-quality assessment;
4. integration of temporally valid exposure and contextual predictors;
5. temporal, spatial, and external validation;
6. uncertainty, calibration, disparity, and feedback-risk evaluation;
7. independent verification of technology-readiness evidence.

## 5. Expected pathway if selected and funded

1. **Institutional authorization:** establish agreements, lawful basis, ethics review, custody, and permitted uses.
2. **Peruvian data integration:** harmonize crime categories, INEI indicators, official territorial units, and lawful urban-context variables.
3. **Comas validation:** extend the district benchmark to safe intradistrict units and evaluate temporal drift and spatial transfer.
4. **Responsible prototype:** create an access-controlled aggregate research interface with uncertainty and human oversight.
5. **Capacity building:** strengthen reproducible geospatial analytics, responsible AI, data governance, and model auditing.
6. **Transfer decision:** determine whether evidence supports later validation; funding alone does not authorize operational use.

## 6. Expected national contribution

The project may contribute locally generated evidence, an auditable alternative to black-box claims, explicit non-use criteria, transparent negative results, and reusable training materials for responsible urban analytics. Transfer beyond Comas requires local recalibration, validation, governance review, and stakeholder authorization.

## 7. Repository alignment

| Requirement | Evidence |
|---|---|
| Applied research problem | `03_protocol/protocol_v1.0.md` |
| Method consistency | `02_method/consistency_matrix.md` |
| Literature evidence | `04_literature/` |
| Official-data benchmark | `05_pipeline/` |
| Reproducibility | `06_repro_audit/` |
| Model limitations | `07_model_card/` |
| Ethics and data governance | `09_ethics/` and `10_data_mgmt/` |
| Bias and impact | `11_bias_audit/` |
| Scientific integrity | `12_integrity/` |

## 8. Update log

| Date | Update | Evidence |
|---|---|---|
| 2026-08-01 | Application context documented. | Applicant-supplied submission record and official call sources. |
| 2026-08-09 | Rapid SLR and public MININTER/SIDPOL benchmark completed. | Search exports, pipeline, forecasts, tests, and executed notebook. |
