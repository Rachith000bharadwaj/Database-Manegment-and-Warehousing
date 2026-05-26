# Database Management and Warehousing: GreenTrace ESG Data Vault

This repository contains the Database Management and Warehousing project **GreenTrace**, an ESG-focused data warehouse system for carbon emissions tracking, carbon credit ledger management, data lineage, and reporting dashboards.

The project demonstrates how an enterprise can organize fragmented sustainability data into a clean, auditable warehouse using **Data Vault 2.0**, then transform that data into business-ready reporting tables and dashboards.

## Project Overview

Organizations often collect sustainability data from many sources: facilities, meters, suppliers, shipments, energy readings, carbon credit transactions, and manual ESG metrics. Without a strong warehouse design, this data becomes difficult to trace, verify, audit, and report.

GreenTrace solves this by building a complete ESG warehouse pipeline:

1. Analyze source datasets.
2. Design a Data Vault 2.0 schema.
3. Load data into MySQL through Python ETL.
4. Calculate Scope 2 and Scope 3 emissions.
5. Maintain a carbon credit ledger.
6. Build a CSRD-style reporting data mart.
7. Track lineage from raw data to final reports.
8. Provide dashboard views for emissions and carbon credit insights.

## Problem Statement

ESG and carbon reporting requires accurate, traceable, and audit-ready data. Many organizations struggle with fragmented spreadsheets, inconsistent source systems, and unclear transformation logic. This can lead to incorrect emissions reporting, double-counted carbon credits, and weak compliance evidence.

This project addresses those issues by creating a structured data warehouse that supports:

- Carbon emissions calculation.
- Scope 2 electricity emissions tracking.
- Scope 3 transportation and supplier activity tracking.
- Carbon credit issue and retirement tracking.
- Data lineage for auditability.
- Reporting-ready data marts.
- Interactive dashboard exploration.

## Repository Structure

```text
.
├── GreenTrace_project/
│   ├── dashboard/
│   │   ├── backend/
│   │   ├── frontend/
│   │   └── run_live_frontend.cmd
│   ├── datasets/
│   │   └── green_trace_export/
│   ├── etl/
│   │   ├── calc_emissions.py
│   │   ├── datamart_pipeline.py
│   │   ├── ledger_pipeline.py
│   │   ├── lineage_pipeline.py
│   │   ├── load_csv_to_mysql.py
│   │   └── support/test scripts
│   ├── reports/
│   │   ├── final_report.md
│   │   ├── phase1_dataset_analysis.md
│   │   ├── phase2_schema_design.md
│   │   ├── phase3_etl_pipeline.md
│   │   ├── phase4_business_vault.md
│   │   ├── phase5_carbon_ledger.md
│   │   ├── phase6_data_mart.md
│   │   ├── phase7_data_lineage.md
│   │   └── phase8_dashboard.md
│   ├── setup/
│   │   ├── .env.example
│   │   ├── debug_schema.py
│   │   └── table_def.txt
│   └── sql/
│       └── create_schema.sql
├── PPT.pptx
├── Report.pdf
└── README.md
```

## Data Warehouse Architecture

GreenTrace uses a **Data Vault 2.0** architecture. This style is useful for warehouse systems that need historical tracking, auditability, scalable loading, and clear relationships between business entities.

### Raw Vault

The Raw Vault stores the core business entities and relationships.

**Hub tables**

- `hub_facility`
- `hub_supplier`
- `hub_meter`
- `hub_shipment`
- `hub_carbon_credit`
- `hub_reporting_period`

**Link tables**

- `link_facility_meter`
- `link_facility_period`
- `link_shipment_supplier_facility`

**Satellite tables**

- `sat_energy_reading`
- `sat_shipment_activity`
- `sat_facility_attr`
- `sat_supplier_attr`
- `sat_carbon_credit_attr`
- `sat_manual_esg_metrics`

### Business Vault

The Business Vault applies logic on top of raw warehouse data. In this project it calculates:

- Scope 2 emissions from electricity and meter readings.
- Scope 3 emissions from shipment, supplier, and transportation activity.

Important tables include:

- `bv_scope2_emission_event`
- `bv_scope3_emission_event`

### Carbon Credit Ledger

The carbon ledger tracks carbon credit issue and retirement events. This helps prevent double counting and allows credit balances to be monitored clearly.

Important tables include:

- `ledger_credit_txn`
- `ledger_credit_position`

### Data Mart

The data mart prepares summarized data for reporting and dashboard use.

Main reporting table:

- `dm_csrds_emissions_summary`

This table aggregates emissions and carbon credit information by facility and reporting period for easier ESG reporting.

### Data Lineage

The lineage layer maps how data moves from source/satellite tables into business vault outputs and final data marts.

Main lineage table:

- `meta_lineage_edge`

This improves auditability by showing how final reporting values were derived.

## Project Phases

### Phase 1: Dataset Analysis

The source data files were inspected and categorized into warehouse-ready entities. The analysis identified business entities such as facilities, suppliers, meters, shipments, reporting periods, emissions factors, and carbon credits.

### Phase 2: Schema Design

A MySQL Data Vault 2.0 schema was designed with hubs, links, satellites, business vault tables, ledger tables, data mart tables, and lineage metadata.

Schema file:

```text
GreenTrace_project/sql/create_schema.sql
```

### Phase 3: ETL Pipeline

Python ETL scripts load CSV data into MySQL. The ETL pipeline handles inspection, loading, validation, duplicate control, and transformation.

Key scripts:

- `load_csv_to_mysql.py`
- `inspect_datasets.py`
- `list_datasets.py`
- `test_dataset.py`
- `test_connection.py`

### Phase 4: Emissions Calculation

The business vault pipeline calculates emissions events from raw activity data and emission factors.

Key script:

- `calc_emissions.py`

### Phase 5: Carbon Credit Ledger

The ledger pipeline records credit issue and retirement events and maintains credit positions.

Key script:

- `ledger_pipeline.py`

### Phase 6: Data Mart Pipeline

The data mart pipeline creates summarized reporting data for ESG/CSRD-style analysis.

Key script:

- `datamart_pipeline.py`

### Phase 7: Data Lineage

The lineage pipeline tracks how source data contributes to final reporting outputs.

Key script:

- `lineage_pipeline.py`

### Phase 8: Dashboard

The dashboard layer provides a frontend and backend for exploring ESG warehouse outputs.

Dashboard folders:

- `GreenTrace_project/dashboard/backend/`
- `GreenTrace_project/dashboard/frontend/`

The frontend includes pages such as:

- `index.html`
- `dashboard.html`
- `architecture.html`

## Technologies Used

- MySQL
- Python
- Pandas
- SQLAlchemy-style ETL workflow
- CSV datasets
- Data Vault 2.0 modeling
- HTML, CSS, and JavaScript dashboard frontend
- Flask-style backend structure
- ESG / CSRD reporting concepts
- Carbon credit ledger modeling

## Dataset Export

The repository includes a generated GreenTrace export under:

```text
GreenTrace_project/datasets/green_trace_export/
```

It contains CSV outputs for:

- Hubs
- Links
- Satellites
- Business vault emission events
- Carbon ledger transactions and positions
- Data mart summaries
- Lineage metadata
- Emission factors

## Setup Notes

Use the environment template as a starting point:

```text
GreenTrace_project/setup/.env.example
```

Typical setup flow:

1. Create a MySQL database.
2. Configure database connection values using `.env.example`.
3. Run the schema script from `sql/create_schema.sql`.
4. Use ETL scripts from `etl/` to load and transform data.
5. Run dashboard backend/frontend files to explore results.

## Documentation

Detailed project phase reports are available in:

```text
GreenTrace_project/reports/
```

Important documents:

- `final_report.md`
- `phase1_dataset_analysis.md`
- `phase2_schema_design.md`
- `phase3_etl_pipeline.md`
- `phase4_business_vault.md`
- `phase5_carbon_ledger.md`
- `phase6_data_mart.md`
- `phase7_data_lineage.md`
- `phase8_dashboard.md`

The repository also includes:

- `Report.pdf`
- `PPT.pptx`

## Project Outcome

GreenTrace provides a complete mini enterprise data warehouse for ESG reporting. It demonstrates how raw operational sustainability data can be modeled, loaded, transformed, audited, and visualized through a structured database management and warehousing workflow.

The final system supports:

- Auditable ESG data storage.
- Scope 2 and Scope 3 emissions calculation.
- Carbon credit ledger tracking.
- Data mart reporting.
- Data lineage.
- Dashboard-based analysis.

