# Completed PRISMA 2020 Flow

**Search date:** August 9, 2026. **Sources:** OpenAlex and Crossref. **Scope:** first 50 relevance-ranked results from each source.

![PRISMA 2020 flow diagram](prisma_flow_diagram.svg)

| Stage | n |
|---|---:|
| Records identified through OpenAlex | 50 |
| Records identified through Crossref | 50 |
| **Total records identified** | **100** |
| Duplicate records removed | 3 |
| Unique records screened | 97 |
| Records excluded by reproducible title rule | 49 |
| Reports sought for retrieval | 48 |
| Reports not retrieved through open access | 10 |
| Reports assessed for eligibility | 38 |
| Full-text reports excluded | 15 |
| **Empirical studies included** | **23** |

## Full-text exclusions

| Primary reason | n |
|---|---:|
| Secondary review without a new empirical study | 5 |
| Insufficient scope or document quality | 6 |
| Predictive validation not verifiable or outside scope | 4 |
| **Total** | **15** |

Consistency check: `100 − 3 = 97`; `97 − 49 = 48`; `48 − 10 = 38`; `38 − 15 = 23`.

Record-level decisions are stored in `screening_log.csv`, the original results in `search_results_2026-08-09.csv`, and the screening rule in `run_literature_search.ps1`. Scopus, Web of Science, IEEE Xplore, ACM Digital Library, and SciELO remain an institutional-access extension. This flow therefore represents a reproducible rapid review and does not claim universal exhaustiveness.
