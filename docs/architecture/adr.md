# Architecture Decision Record

ADR-001: Pipeline Architecture

Date: {{today}}

Status: Accepted

Context
We need to process data from four sources (CSV, JSON, text, Excel) for Newham Public Library. The data has quality issues and needs to be cleaned before it can be used for analysis.

Decision
We will use a medallion architecture with three layers:

Bronze - raw data ingested exactly as received
Silver - cleaned and validated data
Gold - analysis-ready aggregations

## Reasons
We decided to use a Medallion Architecture (Bronze, Silver, Gold) with a dedicated data quality validation step before data reaches the Silver layer. This ensures that only trusted, validated data is used for analysis while preserving the original raw data for auditing and reprocessing.

## Consequences
Raw data is always preserved in bronze - we can reprocess if cleaning logic changes
Silver is the trust boundary - gold always reads from silver, never bronze
We are unsure about how to handle records that fail validation. Should they be automatically quarantined for review, corrected where possible, or rejected entirely? This decision could affect data accuracy and reporting completeness.
