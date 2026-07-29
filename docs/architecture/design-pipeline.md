# Pipeline Architecture Diagram

---
title: Medallion Architecture ~ 4
tags: DE5M5

---
# Medallion Architecture - Group 4

## Task

Create a Mermaid diagram showing how this pipeline should be organised into Bronze, Silver and Gold layers.

Your diagram should show:

- source data
- Bronze layer
- Silver layer
- Gold layer
- at least one data quality or validation step
- at least one final output for a user or stakeholder

## Diagram

```mermaid
flowchart LR

    subgraph Source["Data Sources"]
        Source1[circulation_data.csv]
        Source2[events_data.json]
        Source3[feedback.txt]
        Source4[catalogue.xlsx]
    end

    Bronze[Bronze Layer]

    Source1 --> Bronze
    Source2 --> Bronze
    Source3 --> Bronze
    Source4 --> Bronze

    Check{"Data Quality Checks
    Duplicates
    Missing Values
    Date Formats
    ISBN Validation"}

    Bronze --> Check

    Check -->|Pass| Silver[Silver Layer]
    Check -->|Fail| Quarantine[Quarantine /error records]

    Silver --> Gold[Gold Layer]

    Gold --> Dashboard["Library Analysts
    & Management Dashboard"]
```



## Questions to answer:

### One design decision
- We decided to use a Medallion Architecture (Bronze, Silver, Gold) with a dedicated data quality validation step before data reaches the Silver layer. This ensures that only trusted, validated data is used for analysis while preserving the original raw data for auditing and reprocessing.

### One question or risk
- We are unsure about what to do with the records that are not passing the data quality checks and end up in the quarantine. Will someone review it ? Should they be ignored ?
