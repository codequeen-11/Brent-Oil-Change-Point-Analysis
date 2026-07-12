# Brent Oil Price Change Point Analysis

## Project Overview

This project analyzes historical Brent crude oil prices to identify significant structural changes using Bayesian Change Point Analysis. The objective is to investigate how geopolitical events, economic crises, policy decisions, and global disruptions have influenced oil prices over time.

The project was completed as part of the **10 Academy Artificial Intelligence Mastery Program**.

---

## Business Problem

Birhan Energies seeks to understand how major global events affect Brent crude oil prices. Detecting structural changes in historical prices enables stakeholders to:

- Understand market behavior
- Support investment decisions
- Improve risk management
- Evaluate the impact of geopolitical and economic events
- Develop evidence-based policy recommendations

---

## Project Objectives

The objectives of this project are to:

- Explore historical Brent crude oil prices
- Understand long-term trends and volatility
- Evaluate stationarity of the time series
- Detect structural changes using Bayesian Change Point Analysis
- Associate detected change points with major geopolitical and economic events
- Present findings through an interactive dashboard

---

## Dataset

### Brent Oil Prices

- Daily Brent crude oil prices
- Time period: **May 1987 – September 2022**
- Variables:
  - Date
  - Price (USD per barrel)

### Historical Event Dataset

A curated dataset containing major events that influenced global oil markets, including:

- OPEC production decisions
- Wars and geopolitical conflicts
- Economic crises
- International sanctions
- Pandemics
- Natural disasters

---

## Repository Structure

```text
Brent-Oil-Change-Point-Analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── reports/
│
├── src/
│
├── tests/
│
├── dashboard/
│
├── requirements.txt
│
└── README.md
```

---

## Project Workflow

1. Business Understanding
2. Data Collection
3. Data Preparation
4. Exploratory Data Analysis
5. Time Series Investigation
6. Bayesian Change Point Modeling
7. Event Association
8. Business Interpretation
9. Interactive Dashboard

---

## Exploratory Data Analysis

Task 1 investigates:

- Dataset quality
- Descriptive statistics
- Historical price trends
- Distribution of prices
- Rolling statistics
- Log returns
- Volatility
- Stationarity (ADF and KPSS tests)

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- PyMC
- ArviZ
- Flask
- React

---

## Project Structure

Reusable project components are implemented inside the `src/` package:

- Data loading
- Preprocessing
- Exploratory Data Analysis
- Visualization
- Statistical testing
- Bayesian modeling

This modular design improves maintainability and supports reuse across notebooks and the dashboard.

---

## Key Deliverables

### Task 1

- Project setup
- Workflow documentation
- Exploratory Data Analysis
- Historical event dataset
- Statistical analysis

### Task 2

- Bayesian Change Point Model
- Posterior analysis
- Event comparison

### Task 3

- Flask API
- React Dashboard
- Interactive visualizations

---

## Future Work

Future improvements include:

- Multiple change point detection
- Additional macroeconomic indicators
- Forecasting models
- Real-time dashboard integration

---

## Author

**Aisha Hussein**

Computer Science Graduate

10 Academy AI Mastery Program