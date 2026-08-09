# Research Data Management Plan

## 1. Data categories

| Category | Current example | Classification | Permitted repository |
|---|---|---|---|
| Public official aggregate | MININTER/SIDPOL district-month counts. | Public under source license. | Git or institutional repository with attribution and manifest. |
| Public derived output | Comas summaries, features, forecasts, metrics, and figures. | Public after disclosure and integrity review. | Git/institutional repository. |
| Restricted source | Any future case-level police, municipal, census, or geocoded records. | Confidential or sensitive. | Controlled institutional environment only. |
| Restricted derivative | Small cells, precise coordinates, linkage tables, or revealing model outputs. | Confidential until disclosure risk is resolved. | Controlled institutional environment only. |

## 2. Current public-data record

The repository preserves the official public aggregate file used in the experiment together with its publisher, system, coverage, source URL, license, download date, byte size, and SHA-256 hash in `05_pipeline/docs/source_manifest.csv`. The data dictionary distinguishes published fields from derived analytical fields.

## 3. Responsibilities

The researcher is responsible for license compliance, versioning, integrity checks, accurate scope statements, and preventing inappropriate secondary use. A future institutional data custodian would retain authority over any restricted source data.

## 4. Data life cycle

1. **Acquisition:** record publisher, URL, date, license, version, and hash.
2. **Ingestion:** preserve the downloaded original and validate its schema.
3. **Processing:** use versioned scripts for filtering, aggregation, and feature construction.
4. **Analysis:** record temporal splits, model parameters, seeds, metrics, and outputs.
5. **Review:** verify quality, disclosure risk, licensing, and consistency before publication.
6. **Preservation:** retain permitted data, code, metadata, tests, and results.
7. **Revision:** never silently overwrite a published source version; record a new hash and change log.
8. **Deletion:** apply custodian and ethics requirements to any future restricted data.

## 5. Quality and metadata

Controls cover schema, data types, range, uniqueness, month continuity, UBIGEO membership, category selection, outcome totals, missing values, temporal ordering, and leakage. Automated tests verify the implemented Comas series and features.

## 6. FAIR principles with safeguards

Code, metadata, and lawful aggregates should be findable, interoperable, and reusable. FAIR does not mean that restricted microdata should be public. Any future case-level data, linkage keys, exact coordinates, or small-cell outputs must remain in an approved controlled environment.

## 7. Backup, retention, and disposal

GitHub is acceptable for the current licensed public aggregate and approved derived outputs, but it is not an authorized store for future restricted records. Restricted backups must be encrypted, access-controlled, institutionally approved, and disposed of according to the governing agreement and ethics decision.
