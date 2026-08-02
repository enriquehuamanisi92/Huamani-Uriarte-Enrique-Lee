# Research Data Management Plan

## 1. Data categories

| Category | Example | Classification | Permitted repository |
|---|---|---|---|
| Public synthetic | Generated CSV and demonstration results. | Public; clearly labeled synthetic. | Git/DVC. |
| Public official | Open cartography or tables. | According to license. | Git/DVC or institutional storage. |
| Restricted source | Authorized SIDPOL records. | Confidential/sensitive. | Controlled institutional environment. |
| Restricted derivative | Geocoded data or small cells. | Confidential while disclosure risk exists. | Controlled institutional environment. |
| Publishable derivative | Approved aggregate statistics. | Public after review. | Institutional repository/Git. |

## 2. Responsibilities

The institutional custodian retains authority over source data. The principal investigator is responsible for protocol compliance, access, versioning, and reporting. Collaborators receive only necessary access and formally accept purpose, confidentiality, and incident procedures.

## 3. Data life cycle

1. **Acquisition:** record source, authorization, date, license, and hash.
2. **Ingestion:** validate schemas in an isolated area and preserve originals.
3. **Processing:** versioned scripts create intermediate and analytical layers.
4. **Analysis:** use a controlled environment and record parameters and seeds.
5. **Review:** check quality, disclosure risk, and consistency before export.
6. **Preservation:** retain permitted code, metadata, and outputs.
7. **Deletion:** execute and document the policy agreed with the custodian.

## 4. Metadata and quality

Use ISO 8601 dates, UTF-8, stable non-semantic identifiers, and a declared coordinate reference system. The dictionary will specify name, type, unit, source, transformation, missingness, and sensitivity. Each analytical version will have a hash, commit, date, and owner.

Quality controls cover schemas, ranges, uniqueness, duplicates, missing values, temporal consistency, spatial membership, geocoding rates, and classification changes. Corrections will be scripted; manual changes require an audit log.

## 5. FAIR principles with safeguards

The project will maximize findability, controlled accessibility, interoperability, and reuse of code and metadata. FAIR does not mean open sensitive data. Microdata will remain restricted; synthetic data, dictionaries, and safe authorized aggregates may be published.

## 6. Backup, retention, and disposal

Backups will be encrypted, versioned, institutionally approved, and periodically restored in tests. Git is not an authorized backup for real data. The retention period will be defined in the agreement and ethics approval. At closure, unnecessary working copies, credentials, and keys will be verifiably removed.
