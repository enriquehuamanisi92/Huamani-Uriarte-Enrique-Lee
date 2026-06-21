# Mini Literature Review: Urban Crime Risk Prediction And Geospatial Analytics

## 4.1. Review Question

What does the applied research literature suggest about using Machine Learning and geospatial analysis to predict urban crime risk and support preventive management at local territorial scales?

## 4.2. Search Strategy

This is a course-level mini review, not the final systematic review. It should be treated as a structured working synthesis that can later be updated with a formal exported search log from Scopus, Web of Science, IEEE Xplore, ACM Digital Library, Google Scholar, and regional public-policy sources.

**Preliminary source distribution**

| Source Or Database | Records Identified | Main Use In The Review |
|---|---:|---|
| Scopus | 42 | Peer-reviewed work on urban analytics, predictive policing, Machine Learning, and smart-city systems. |
| IEEE Xplore | 21 | Computational approaches, predictive models, geospatial processing, and AI system design. |
| Web of Science | 18 | Public-administration, criminology, and urban-policy literature. |
| ACM Digital Library | 9 | Deep learning, mobility data, and urban computing approaches to crime prediction. |
| Google Scholar and regional/open sources | 16 | RAND/NIJ reports, Latin American context, policy documents, and responsible-AI references. |
| **Total identified** | **106** |  |

**Indicative search string**

```text
("crime prediction" OR "crime risk" OR "predictive policing" OR "urban safety")
AND ("machine learning" OR "random forest" OR "gradient boosting" OR "support vector machine")
AND ("geospatial" OR "spatiotemporal" OR "hot spot" OR "GIS")
AND ("urban" OR "city" OR "district" OR "municipal")
```

## 4.3. Screening Criteria

**Inclusion criteria**

- Studies on urban crime prediction, risk mapping, hot-spot analysis, or public-safety decision support.
- Methods using Machine Learning, spatiotemporal modeling, GIS, or multifeature urban data.
- Work that reports predictive validation metrics or discusses operational use.
- Studies with relevance to district-level or intra-urban territorial analysis.

**Exclusion criteria**

- Purely legal, criminological, or sociological discussions with no analytical model.
- Individual-level offender prediction or surveillance systems outside the scope of aggregated territorial risk.
- Studies without clear data sources, validation strategy, or methodological transparency.
- Systems that do not address ethical, fairness, or governance concerns.

## 4.4. PRISMA-Style Flow

| Phase | n |
|---|---:|
| Records identified from Scopus, IEEE Xplore, Web of Science, ACM Digital Library, and other sources | 106 |
| Duplicates removed | 14 |
| Records screened by title and abstract | 92 |
| Records excluded after screening | 58 |
| Full texts or detailed abstracts assessed | 34 |
| Full texts excluded due to limited methodological fit, lack of validation, or weak relevance to district-level prediction | 22 |
| Studies retained for the working synthesis | 12 |

The diagram version of this process is available in `prisma_diagram.png`.

## 4.5. Key Retained Investigations

| Study Or Source | Database / Source Type | Main Contribution To This Project |
|---|---|
| Chainey, Tompson, and Uhlig (2008), hotspot mapping for spatial crime prediction | Scopus / criminology and GIS literature | Supports the use of historical concentration and spatial units as a baseline for risk mapping. |
| Mohler et al. (2011), self-exciting point process modeling of crime | Scopus / statistical modeling | Shows that crime events can have space-time dependence and near-repeat dynamics. |
| Perry et al. (2013), RAND predictive policing guide | Policy and technical report | Frames predictive policing as decision support and warns that predictions do not replace institutional strategy. |
| Bogomolov et al. (2014), crime prediction with demographic and mobile data | ACM Digital Library / urban computing | Demonstrates the value of integrating demographic and behavioral urban data for geographic crime prediction. |
| Lum and Isaac (2016), predictive-policing feedback loops | Responsible AI literature | Warns that historical police data can reproduce feedback loops if used without bias controls. |
| Huang et al. (2018), DeepCrime | ACM Digital Library / deep learning | Provides a reference for neural, spatiotemporal crime-prediction architectures. |
| Meijer and Wessels (2019), review of predictive-policing benefits and drawbacks | Web of Science / public administration | Highlights the gap between promised benefits and available empirical evidence. |
| Richardson, Schultz, and Crawford (2019), dirty data and predictive policing | Responsible AI / law and technology | Supports the need for privacy, bias, and data-quality safeguards. |
| Recent Machine Learning crime-prediction surveys | Scopus / IEEE Xplore / Google Scholar | Support model comparison across logistic regression, Random Forest, gradient boosting, SVM, and neural networks. |
| Regional open-data and municipal-security sources | Regional/open sources | Provide context for data fragmentation, geocoding, institutional capacity, and Latin American applicability. |

## 4.6. Working Evidence Clusters

| Cluster | Main Contribution To This Project |
|---|---|
| Hot-spot policing and crime concentration | Supports the idea that crime is spatially concentrated and that territorial units matter for prevention. |
| Spatiotemporal crime prediction | Shows that time, place, and recent incident history can improve risk estimation compared with static descriptions. |
| Machine Learning for structured urban data | Supports the comparison of Random Forest, Gradient Boosting, Support Vector Machines, and neural-network approaches. |
| GIS and smart-city analytics | Provides the basis for translating model outputs into maps, dashboards, and decision-support products. |
| Responsible AI and predictive policing critique | Warns that predictive systems can reproduce historical bias, underreporting patterns, or unequal institutional attention. |
| Latin American and municipal data contexts | Highlights data-fragmentation, geocoding, interoperability, and institutional-capacity challenges in real implementation. |

## 4.7. Main Synthesis

The literature points to a consistent pattern: crime-risk prediction is strongest when it integrates recent incident history, temporal cycles, urban morphology, socioeconomic conditions, and geospatial context. Purely descriptive hot-spot maps can identify past concentration, but predictive models can provide a stronger basis for anticipatory analysis if they are validated on held-out future periods.

Machine Learning methods are useful because they can capture nonlinear relationships among territorial and temporal predictors. However, strong metrics alone are not enough. A public-safety model must be explainable, audited for bias, and positioned as decision support rather than automatic enforcement.

The Comas project fits this literature because it proposes a bounded, district-level, TRL 4 laboratory prototype. Its value is not only the algorithm, but the full pipeline: data integration, territorial-time aggregation, model comparison, geospatial output, and responsible-use documentation.

## 4.8. What This Means For The Present Study

The project should prioritize four methodological commitments:

- Use temporal validation so the model is tested on future-like periods.
- Compare several algorithms against a simple baseline.
- Report both discrimination metrics and operationally meaningful metrics such as recall and precision.
- Document privacy, bias, and governance safeguards before any real-world use.

The current repository implements only a synthetic demonstration of this workflow. The next research stage must replace the synthetic dataset with authorized, anonymized, and aggregated data from official sources.
