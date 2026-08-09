# Datasheet — Public MININTER/SIDPOL Police Reports

## Motivation

This dataset supports a reproducible district-level forecasting benchmark for Comas using official public aggregates. It is not individual-level police microdata.

## Source and provenance

- **Publisher:** Ministry of the Interior of Peru.
- **Originating system:** Police Complaints Information System (SIDPOL).
- **Public portal:** https://www.datosabiertos.gob.pe/dataset/denuncias-policiales-1
- **License:** Open Data Commons Attribution License.
- **Coverage used:** January 2018–May 2026.
- **Downloaded:** August 9, 2026.
- **File size:** 26,896,357 bytes.
- **SHA-256:** `CDC6D3D32A37A00FF7F2F1D15D65512FEC3A36A0291BB67FEDE482CA1FFB22BC`.

## Composition

The national file contains year, month, department, province, district, UBIGEO, published report category, and count. The Comas subset is selected with UBIGEO `150110`. The implemented outcome uses `Hurto` and `Robo` only.

| Item | Value |
|---|---:|
| Comas rows across all categories | 698 |
| Monthly periods | 101 |
| Theft reports | 22,934 |
| Robbery reports | 24,620 |
| Combined analytical outcome | 47,554 |

## Processing

Code pivots the two categories to one row per month, completes the monthly calendar, calculates shifted lags and rolling means, and defines the following month as the target. All transformations are implemented in `05_pipeline/src/train.py`.

## Personal data and sensitivity

The public table contains no names, identity numbers, addresses, individual coordinates, victims, suspects, or record-level case descriptions. Nevertheless, public availability does not make the measurements neutral or suitable for unrestricted inference.

## Known limitations

- Reports are not equivalent to all crime events.
- Classification and recording practices may change over time.
- District aggregation prevents intradistrict spatial analysis.
- The dataset does not include monthly population exposure or contextual predictors.
- The pandemic period and subsequent drift affect comparability.
- Publisher updates may differ from the frozen file; use the recorded hash for exact reproduction.

## Permitted use

Permitted uses include reproducible research, aggregate trend analysis, method comparison, and educational evaluation under the source license. The dataset and derived forecasts must not be used to profile individuals, infer guilt, stigmatize communities, or automate enforcement decisions.
