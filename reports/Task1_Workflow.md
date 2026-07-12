# Task 1: Analysis Workflow – Brent Oil Price Change Point Analysis

## 1. Introduction

Brent crude oil is one of the world's most important benchmark commodities, influencing global energy markets, investment decisions, and economic policies. Its price is affected by numerous geopolitical, economic, and policy-related events, including armed conflicts, OPEC production decisions, international sanctions, financial crises, and global pandemics. Understanding when significant structural changes occur in oil prices and identifying the events that may have contributed to those changes can provide valuable insights for investors, policymakers, and energy companies.

This project aims to analyze historical Brent oil prices using Bayesian Change Point Analysis to detect statistically significant structural breaks in the time series. The detected change points will then be compared with major historical events to investigate potential relationships between market behavior and external factors.

---

# 2. Business Understanding

Birhan Energies seeks to understand how major geopolitical and economic events influence Brent crude oil prices. The objective is not only to identify periods of significant price changes but also to quantify those changes and provide evidence-based insights that support strategic decision-making.

The project addresses the following business questions:

* When did significant structural changes occur in Brent oil prices?
* Which geopolitical or economic events coincide with these structural changes?
* How large were the changes before and after each detected event?
* How can these findings support investment, policy, and operational planning?

---

# 3. Data Sources

The analysis will utilize two primary datasets:

**Historical Brent Oil Prices**

The main dataset contains daily Brent crude oil prices from May 1987 to September 2022. Each observation includes the trading date and the corresponding price in USD per barrel.

**Historical Event Dataset**

An external dataset will be created containing major geopolitical events, OPEC policy decisions, economic crises, international sanctions, and global conflicts that are expected to influence oil prices. Each event will include the event date, category, description, and expected market impact.

---

# 4. Analysis Workflow

The project will follow a structured data science workflow consisting of the following stages.

### Step 1 – Data Understanding

The Brent oil price dataset will be inspected to understand its structure, identify missing values, verify data types, and ensure that the observations are chronologically ordered. Descriptive statistics will be generated to summarize the overall characteristics of the data.

### Step 2 – Data Preparation

The Date column will be converted into a datetime format and used as the time index. Data quality checks will be performed to identify duplicates or inconsistencies. Logarithmic returns will also be calculated to support statistical analysis where appropriate.

### Step 3 – Exploratory Data Analysis

Exploratory analysis will be conducted to understand the long-term behavior of Brent oil prices. Time series plots, rolling statistics, distribution analysis, and volatility visualizations will be used to identify major trends and potential structural changes.

### Step 4 – Time Series Investigation

Before constructing the Bayesian model, important statistical properties of the series will be evaluated. This includes trend analysis, stationarity testing, and volatility assessment. These investigations will help determine whether transformations such as log returns are appropriate for modeling.

### Step 5 – Bayesian Change Point Modeling

A Bayesian Change Point model will be developed using PyMC to estimate the probability of structural changes occurring throughout the historical price series. The model will estimate the change point location together with the average behavior of the series before and after the detected change.

### Step 6 – Event Association

Detected change points will be compared with the historical event dataset. Where a structural break occurs close to a major geopolitical or economic event, a hypothesis will be formulated regarding the possible relationship between the event and the observed price change.

### Step 7 – Interpretation and Business Insights

The statistical findings will be translated into business insights by explaining the magnitude of each detected change and discussing its potential implications for investors, policymakers, and energy companies.

### Step 8 – Dashboard Development

The final results will be presented through an interactive dashboard consisting of a Flask backend and a React frontend. The dashboard will enable users to explore historical prices, detected change points, and related geopolitical events through interactive visualizations.

---

# 5. Assumptions

The analysis is based on the following assumptions:

* The historical Brent oil price dataset accurately represents daily market prices.
* Event dates collected from reliable public sources are sufficiently accurate for temporal comparison.
* Significant structural changes in the time series may correspond to important geopolitical or economic events.
* Bayesian Change Point Analysis can identify statistically meaningful structural breaks within the observed time series.
* Daily oil prices are sufficient for detecting long-term structural changes without requiring intraday data.

---

# 6. Limitations

Several limitations should be considered when interpreting the results.

* A temporal relationship between an event and a detected change point does not prove causality.
* Oil prices are influenced by many interacting factors, including supply, demand, exchange rates, inflation, investor sentiment, and macroeconomic conditions, many of which are not explicitly included in this analysis.
* Some events have delayed or gradual effects rather than immediate impacts.
* The Bayesian model identifies statistical changes in the data but cannot determine the exact real-world cause of those changes without additional evidence.

---

# 7. Correlation versus Causation

An important objective of this project is to distinguish between correlation and causation.

If a detected change point occurs close to the date of a geopolitical event, this indicates a temporal association rather than definitive proof that the event caused the price change. Other unobserved factors may have contributed to the observed behavior. Therefore, this analysis should be interpreted as identifying statistically significant relationships that generate evidence-based hypotheses rather than establishing direct causal effects.

---

# 8. Expected Outcomes

The project is expected to produce:

* A cleaned and well-documented Brent oil price dataset.
* A structured dataset of major geopolitical and economic events.
* Exploratory visualizations illustrating long-term trends and volatility.
* Bayesian estimates of significant structural change points.
* Quantitative comparisons of oil prices before and after major structural changes.
* Business insights explaining how historical events may have influenced Brent oil prices.
* An interactive dashboard that enables stakeholders to explore the analytical results.

