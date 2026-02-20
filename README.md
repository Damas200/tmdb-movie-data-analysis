#  TMDb Movie Data Analysis using Pandas & APIs

## Project Overview

This project implements a modular, production-style data pipeline to extract, transform, analyze, and visualize movie performance data using the **TMDb (The Movie Database) API**.

The system follows a structured ETL architecture and emphasizes:

* Separation of concerns
* Reproducibility
* Structured logging
* Data validation
* Feature engineering
* KPI persistence
* Analytical visualization

The goal is to evaluate financial performance, investment efficiency, audience engagement, franchise impact, and temporal revenue trends using engineered metrics.

---

#  System Architecture

```text
TMDb API
   ↓
Extraction Layer (api_client.py)
   ↓
Cleaning Layer (data_cleaning.py)
   ↓
Feature Engineering (feature_engineering.py)
   ↓
KPI Analytics (kpi_analysis.py)
   ↓
Visualization Layer (visualization.py)
   ↓
CSV Outputs + Reports
```

---

#  Project Structure

```text
TMDB_Movie_Data_Analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── kpis/
│
├── notebooks/
│   └── analysis.ipynb
│
├── reports/
│   ├── kpis/
│   │   └── kpi_summary.md
│   └─
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── api_client.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── kpi_analysis.py
│   ├── visualization.py
│   ├── logger_config.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

#  Key Features

##  1. API Data Extraction

* Fetches movie metadata from TMDb
* Retrieves cast and crew (director extraction included)
* Handles API errors and timeouts
* Uses `.env` for secure API key management

##  2. Data Cleaning & Transformation

* JSON flattening (genres, production companies, languages, etc.)
* Data type enforcement
* Zero-value replacement for financial fields
* Released-movie filtering
* Deduplication using stable identifiers
* Data completeness enforcement

##  3. Feature Engineering

* Budget & Revenue conversion to million USD
* Profit calculation
* ROI (Return on Investment)
* Release year & decade extraction
* Franchise flag creation

##  4. KPI Analytics

Automatically computes and saves:

* Top/Bottom Revenue
* Top/Bottom Budget
* Top/Bottom Profit
* Top/Bottom ROI
* Most Voted
* Highest & Lowest Rated
* Most Popular
* Franchise vs Standalone comparison
* Most Successful Franchises
* Most Successful Directors

All KPI tables are exported to:

```text
data/kpis/
```

---

##  5. Visualization

Implemented plots:

* Revenue vs Budget (with regression)
* ROI distribution by genre
* Popularity vs rating
* Yearly revenue trends
* Franchise vs standalone comparison

Visualizations are generated in:

```text
notebooks/analysis.ipynb
```

---

## 6. Structured Logging

The pipeline uses centralized logging:

* Console logs
* File logs (`logs/pipeline.log`)
* Timestamped execution tracking
* Error-level handling

---

# Outputs Generated

After running:

```bash
python main.py
```

The following are produced:

### Raw Dataset

```
data/raw/movies_raw.csv
```

### Processed Dataset

```
data/processed/movies_processed.csv
```

### KPI Tables

```
data/kpis/*.csv
```

### Logs

```
logs/pipeline.log
```

---

#  Installation Guide

## 1️. Clone Repository

```bash
git clone <repository-url>
cd TMDB_Movie_Data_Analysis
```

## 2️. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️. Add TMDb API Key

Create a `.env` file:

```text
TMDB_API_KEY=your_api_key_here
```

Get your API key from:
[https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

---

#  Running the Pipeline

Execute full ETL workflow:

```bash
python main.py
```

---

#  Running the Analysis Notebook

Launch Jupyter:

```bash
jupyter notebook
```

Open:

```
notebooks/analysis.ipynb
```

Ensure the project root is added to `sys.path` if needed.

---

# Key Analytical Insights

* Strong positive relationship between budget and revenue.
* Fantasy and Romance genres exhibit highest median ROI.
* Popularity does not strictly correlate with rating.
* Modern revenue concentration is franchise-driven.
* Standalone films can produce extreme outlier success.
* Franchise films demonstrate performance stability.

---

#  Limitations

* Dataset limited to selected blockbuster movie IDs.
* Inflation adjustments not applied.
* Popularity metric specific to TMDb.
* Results are not representative of full industry data.

---

#  Technologies Used

* Python 3.12
* Pandas 2.x
* NumPy
* Requests
* Matplotlib
* Seaborn
* python-dotenv
* Logging module

---

#  Author

**Damas Niyonkuru**
Data Engineering & Analytics Mini-Project


