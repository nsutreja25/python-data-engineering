# python-data-engineering
A Python Data Engineering portfolio focused on the oil &amp; gas industry. This repository showcases hands-on projects using Python, pandas, NumPy, and Jupyter Notebook to build ETL workflows, clean and transform operational data, perform data quality validation, and create analytics-ready datasets from realistic industry scenarios.

# Oil & Gas Data Engineering Portfolio

This repository showcases my journey in learning and applying Python for Data Engineering through realistic oil & gas use cases.

The projects demonstrate core data engineering concepts including data ingestion, cleaning, transformation, validation, exploratory analysis, and ETL pipeline development using Python, pandas, NumPy, and Jupyter Notebook. The goal is to build practical, production-oriented solutions that reflect common data engineering challenges in the energy industry.

## Technologies
- Python
- pandas
- NumPy
- Jupyter Notebook
- Git & GitHub

## Topics Covered
- Python Fundamentals
- NumPy for numerical computing
- pandas for data manipulation
- Data Cleaning & Validation
- Exploratory Data Analysis (EDA)
- Time Series Analysis
- ETL Pipelines
- CSV Processing
- API ingestion
- Data Quality Checks

## Ingestion

Implemented the initial data ingestion layer for the Oil & Gas Data Engineering platform. The ingestion framework retrieves energy datasets from external sources, handles API communication, converts raw responses into structured pandas DataFrames, and persists raw datasets for downstream processing.

The current implementation focuses on integrating the **U.S. Energy Information Administration (EIA) Open Data API** as the primary data source.


## Data Sources
### 1. EIA Open Data API
The pipeline connects to the EIA REST API to retrieve publicly available energy datasets, including:
- Crude oil production data
- Natural gas production data
- Energy market statistics

API documentation:
https://www.eia.gov/opendata/

---

## Ingestion Workflow
The ingestion process follows a standard ETL pattern:

### API Authentication

- API credentials are securely managed using environment variables.
- API keys are stored in `.env` files and are not committed to source control.
- Configuration management is handled through a centralized configuration module.

### API Request Handling

The ingestion module uses Python's `requests` library to communicate with the EIA API.
Implemented features:

- REST API GET requests
- API key authentication
- Request timeout handling
- HTTP error handling
- Response validation

