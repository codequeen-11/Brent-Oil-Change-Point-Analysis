"""
Functions for loading datasets.
"""

import pandas as pd


def load_brent_data(filepath):
    """
    Load Brent oil price dataset.

    Parameters
    ----------
    filepath : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    df = pd.read_csv(filepath)

    return df


def validate_dataset(df):
    """
    Display dataset validation information.
    """

    print("=" * 50)
    print("Dataset Validation")
    print("=" * 50)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())