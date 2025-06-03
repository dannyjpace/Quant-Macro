
# MSc Thesis Project: Macro-Forecasting-Driven Investment Strategy  
**Author: Daniel J. Pace**

---

## Objective

This project is designed as a comprehensive, multi-layered system to build a quantitative investment strategy driven by macroeconomic forecasts. The approach integrates traditional macroeconomic indicators with AI-augmented features, sentiment analysis, real-time alternative datasets, and geopolitical risk signals to dynamically allocate capital across asset classes including equities, fixed income, commodities, and foreign exchange.

The overarching goal is to deliver a modular, scalable framework that systematically outperforms static allocation models through macro-forecast-informed decision-making.

---

## High-Level Architecture

The project follows a five-layer architecture. Each layer progressively enriches the informational content available to forecasting and allocation models:

```
data/
├── Layer 1 - Core Macro                # Macroeconomic fundamentals
├── Layer 2 - AI Augmentation           # Engineered features (lags, PCA, etc.)
├── Layer 3 - Sentiment Analysis        # Textual signals from policy discourse
├── Layer 4 - Alternative Real-Time Data# High-frequency indicators
├── Layer 5 - Geopolitical Risk Index   # Global geopolitical risk structure
```

Each layer feeds into forecasting, allocation, and evaluation components.

---

## Folder Structure

### `data/` — Central repository for all datasets

Each region (US, Euro Area, China) has:

```
├── raw/        # Original downloaded CSVs
├── cleaned/    # Aligned and cleaned datasets (e.g., imputed, reindexed)
├── features/   # Engineered variables for modeling
├── meta/       # Metadata and source documentation
```

Also includes:
- `cross_country/` for harmonized panel data
- `download_data.py` to fetch and update data

---

## Layer-by-Layer Breakdown

### Layer 1 – Core Macro

**Purpose:** To collect and align core macroeconomic variables for each region including GDP, inflation, interest rates, unemployment, consumption, and labor participation.

**Process:**
- CSVs are collected and placed into `raw/`
- Files are cleaned and aligned using Jupyter notebooks and saved into `cleaned/`
- Lagged or transformed features can be created and stored in `features/`

**Examples:**
- `gdp_quarterly.csv`
- `fed_funds_rate.csv`
- `unemployment_rate.csv`

### Layer 2 – AI Augmentation

**Purpose:** To enrich macro data using data science techniques:
- Lag features
- Moving averages
- Differencing
- Principal Component Analysis (PCA)
- Volatility features

These enhancements transform time series into ML-ready tabular datasets used in XGBoost, LSTM, and VAR models.

### Layer 3 – Sentiment Analysis

**Sources:** 
- Central bank speeches
- IMF and World Bank economic outlooks

**Methods:**
- NLP using spaCy or transformer models
- Lexicon-based scoring
- Topic modeling

**Output:**
- Policy tone indices
- Confidence shifts
- Narrative sentiment trajectories

### Layer 4 – Alternative Real-Time Data

**Sources:**
- Job postings data
- Mobility trends
- Real-time energy consumption
- Maritime traffic

**Purpose:** To capture signals missed by lagging government reports and detect turning points earlier.

**Models:** Kalman filters, LSTMs, and advanced signal processing for nowcasting.

### Layer 5 – Geopolitical Risk Index

**Inspired by:** Caldara & Iacoviello (2022)

**Components:**
- Country-level GPR scores
- Trade and defense graphs
- Risk propagation networks

**Use:** Quantify geopolitical volatility and integrate it as a systematic macro risk input.

---

## Modeling Pipeline

### Forecasting Engine
- Inputs: Layers 1 through 5
- Methods: ARIMA, VAR, Bayesian VAR, XGBoost, LSTM
- Outputs: Predicted GDP, inflation, interest rates, labor data

### Forecast Integration
- Meta-learners, ensemble models, and Bayesian model averaging combine different forecasts into a unified macro outlook.

### Asset Allocation
- A scoring model maps macro regimes to asset classes
- Risk-adjusted optimization (e.g., volatility targets)
- Monthly rebalancing

### Backtesting
- Benchmarks: 60/40 portfolio, factor-tilted strategies
- Metrics: Sharpe ratio, Sortino ratio, drawdowns, turnover, CAGR

---

## Notebooks

| Notebook                                | Purpose                                   |
|----------------------------------------|-------------------------------------------|
| `00_clean_and_explore_macro_data.ipynb`| Load and inspect raw macro data           |
| `01_explore_macro_data.ipynb`          | Visualize macro indicators                |
| `02_sentiment_analysis.ipynb`          | Extract textual sentiment from policy     |
| `03_geopolitical_risk.ipynb`           | Build geopolitical risk index             |
| `04_model_comparison.ipynb`            | Evaluate forecasting model performance    |

---

## `src/` Codebase

| Subfolder        | Description                                           |
|------------------|-------------------------------------------------------|
| `src/data/`      | Utilities for transforming and loading macro data     |
| `src/models/`    | Forecasting models (e.g., ARIMA, XGBoost, LSTM)       |
| `src/allocation/`| Portfolio allocation logic                            |
| `src/backtest/`  | Simulates strategy performance over historical periods|

This modular setup allows reusable, production-quality logic separated from exploratory notebooks.

---

## `dashboard/` (Optional)

An optional web dashboard built in Streamlit provides an interactive interface for:
- Uploading new forecasts
- Visualizing macro trends
- Exploring historical allocations and backtested performance

---

## `reports/`

- `figures/`: Output charts and graphics used in the final thesis
- `thesis_analysis.pdf`: Final write-up submitted for academic review

---

## How We Get the Data

Data is collected using the script `download_data.py`, which fetches updated macroeconomic series from APIs (e.g., FRED, ECB), CSV dumps (e.g., IMF, World Bank), and web portals (e.g., OECD, Eurostat). This script ensures consistent formatting and storage into the `raw/` subfolders of each region.

Sentiment data is scraped or downloaded from speech repositories and reports, while real-time data is pulled from open APIs or tracked manually via export from tools such as Google Mobility Reports or public electricity grids.

---

## Why This Layered Design Works

Each layer independently contributes predictive signal strength and resilience. Together, they provide:
- Redundancy and robustness in signals
- Flexibility to test hypotheses and isolate model value-add
- Theoretical coverage across traditional, behavioral, and real-time economics

This ensures methodological soundness and practical scalability — a requirement for both academic and institutional applications.

---

## Final Aim

To evaluate whether an integrated macro-forecasting investment framework can consistently outperform static asset allocation, and to provide a foundation for future work in systematic macro investing for hedge funds, public policy, or sovereign wealth management.

