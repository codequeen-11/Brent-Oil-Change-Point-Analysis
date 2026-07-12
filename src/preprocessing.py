# import numpy as np


# def preprocess_data(df):
#     """
#     Clean and prepare dataset.
#     """

#     df = df.copy()

#     df["Date"] = pd.to_datetime(df["Date"])

#     df = df.sort_values("Date")

#     df.reset_index(drop=True, inplace=True)

#     df["Log_Price"] = np.log(df["Price"])

#     df["Log_Return"] = df["Log_Price"].diff()

#     return df

"""
Data preprocessing functions.
"""

import numpy as np
import pandas as pd


def preprocess_data(df):
    """
    Clean and prepare Brent oil dataset.
    """

    df = df.copy()

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by date
    df = df.sort_values("Date")

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Create log price
    df["Log_Price"] = np.log(df["Price"])

    # Create log returns
    df["Log_Return"] = df["Log_Price"].diff()

    return df