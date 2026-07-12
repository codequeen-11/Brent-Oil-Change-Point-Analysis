"""
Exploratory data analysis helper functions.
"""

import pandas as pd


def dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Start Date": df["Date"].min(),
        "End Date": df["Date"].max(),
    }

    return summary


def descriptive_statistics(df):

    return df["Price"].describe()


def missing_values(df):

    return df.isnull().sum()


def rolling_statistics(df, window=30):

    rolling_mean = df["Price"].rolling(window).mean()

    rolling_std = df["Price"].rolling(window).std()

    return rolling_mean, rolling_std