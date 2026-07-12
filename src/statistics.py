"""
Statistical analysis functions.
"""

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss


def adf_test(series):

    result = adfuller(series.dropna())

    return {
        "ADF Statistic": result[0],
        "p-value": result[1],
        "Critical Values": result[4],
    }


def kpss_test(series):

    statistic, p_value, lags, critical = kpss(series.dropna(), regression="c")

    return {
        "KPSS Statistic": statistic,
        "p-value": p_value,
        "Critical Values": critical,
    }