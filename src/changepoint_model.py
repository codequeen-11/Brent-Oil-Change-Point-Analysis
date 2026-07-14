
"""
Bayesian Change Point Analysis using PyMC.

This module provides reusable functions for detecting a single structural
change in a time series using Bayesian inference.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------------------

def prepare_series(
    df: pd.DataFrame,
    column: str = "Log_Return",
) -> np.ndarray:
    """
    Prepare a numeric time series for Bayesian modeling.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.

    column : str
        Column to model.

    Returns
    -------
    np.ndarray
    """

    if column not in df.columns:
        raise ValueError(f"'{column}' column not found.")

    series = df[column].dropna().to_numpy()

    if len(series) < 30:
        raise ValueError("Time series is too short.")

    return series


# ---------------------------------------------------------------------
# Model Construction
# ---------------------------------------------------------------------

def build_change_point_model(
    series: np.ndarray,
) -> pm.Model:
    """
    Build a Bayesian single change point model.

    Parameters
    ----------
    series : np.ndarray

    Returns
    -------
    pm.Model
    """

    n = len(series)

    idx = np.arange(n)

    with pm.Model() as model:

        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n - 1,
        )

        mu_1 = pm.Normal(
            "mu_1",
            mu=np.mean(series),
            sigma=np.std(series) * 2,
        )

        mu_2 = pm.Normal(
            "mu_2",
            mu=np.mean(series),
            sigma=np.std(series) * 2,
        )

        sigma = pm.HalfNormal(
            "sigma",
            sigma=np.std(series),
        )

        mu = pm.math.switch(
            tau >= idx,
            mu_1,
            mu_2,
        )

        # pm.Normal(
        #     "likelihood",
        #     mu=mu,
        #     sigma=sigma,
        #     observed=series,
        # )
        nu = pm.Exponential("nu", 1 / 30)
        pm.StudentT(
    "likelihood",
    nu=nu,
    mu=mu,
    sigma=sigma,
    observed=series,
)
        

    return model


# ---------------------------------------------------------------------
# Sampling
# ---------------------------------------------------------------------

def sample_model(
    model: pm.Model,
    draws: int = 1500,
    tune: int = 2000,
    chains: int = 4,
    cores: int = 2,
    target_accept: float = 0.99,
    random_seed: int = 42,
):
    """
    Run MCMC sampling.
    """

    with model:

        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=chains,
            cores=cores,
            target_accept=target_accept,
            random_seed=random_seed,
            return_inferencedata=True,
        )

    return trace


# ---------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------

def summarize_trace(trace) -> pd.DataFrame:
    """
    Return posterior summary.
    """
    # series = (series - series.mean()) / series.std()
    return az.summary(
        trace,
        var_names=[
            "tau",
            "mu_1",
            "mu_2",
            "sigma",
        ],
    )


# ---------------------------------------------------------------------
# Trace Plot
# ---------------------------------------------------------------------

def plot_trace(trace):

    az.plot_trace(
        trace,
        var_names=[
            "tau",
            "mu_1",
            "mu_2",
            "sigma",
        ],
    )

    plt.tight_layout()

    plt.show()


# ---------------------------------------------------------------------
# Posterior Plot
# ---------------------------------------------------------------------

def plot_posterior(trace):

    az.plot_posterior(
        trace,
        var_names=[
            "tau",
            "mu_1",
            "mu_2",
            "sigma",
        ],
    )

    plt.tight_layout()

    plt.show()


# ---------------------------------------------------------------------
# Change Point
# ---------------------------------------------------------------------

def get_change_point_index(trace) -> int:
    """
    Return posterior mean change point index.
    """

    tau = trace.posterior["tau"].values.flatten()

    return int(np.round(np.mean(tau)))


def get_change_point_date(
    df: pd.DataFrame,
    trace,
) -> pd.Timestamp:
    """
    Convert change point index into date.
    """

    idx = get_change_point_index(trace)

    return df.iloc[idx]["Date"]


# ---------------------------------------------------------------------
# Impact Analysis
# ---------------------------------------------------------------------

def quantify_change(
    df: pd.DataFrame,
    trace,
    value_column: str = "Price",
) -> dict:
    """
    Compare mean values before and after the change point.
    """

    change_date = get_change_point_date(df, trace)

    before = df[df["Date"] < change_date][value_column]

    after = df[df["Date"] >= change_date][value_column]

    before_mean = before.mean()

    after_mean = after.mean()

    percent_change = (
        (after_mean - before_mean)
        / before_mean
    ) * 100

    return {

        "change_date": change_date,

        "before_mean": before_mean,

        "after_mean": after_mean,

        "percent_change": percent_change,

    }


# ---------------------------------------------------------------------
# Event Matching
# ---------------------------------------------------------------------

def associate_events(
    change_date,
    events: pd.DataFrame,
    window: int = 30,
):
    """
    Find historical events near the detected change point.
    """

    events = events.copy()

    events["Date"] = pd.to_datetime(events["Date"])

    start = change_date - pd.Timedelta(days=window)

    end = change_date + pd.Timedelta(days=window)

    return events[
        (events["Date"] >= start)
        &
        (events["Date"] <= end)
    ]


# ---------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------

def plot_change_point(
    df: pd.DataFrame,
    trace,
    value_column: str = "Price",
    save_path: Optional[str] = None,
):
    """
    Plot detected change point.
    """

    change_date = get_change_point_date(df, trace)

    plt.figure(figsize=(15,6))

    plt.plot(
        df["Date"],
        df[value_column],
        label=value_column,
    )

    plt.axvline(
        change_date,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Change Point\n{change_date.date()}",
    )

    plt.title("Detected Bayesian Change Point")

    plt.xlabel("Date")

    plt.ylabel(value_column)

    plt.legend()

    plt.grid(True)

    if save_path:

        Path(save_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()