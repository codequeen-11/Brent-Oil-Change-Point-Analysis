from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data"


def get_prices():

    df = pd.read_csv(
        DATA / "raw" / "BrentOilPrices.csv"
    )

    df["Date"] = pd.to_datetime(df["Date"])

    return (
        df[["Date", "Price"]]
        .assign(Date=lambda d: d["Date"].dt.strftime("%Y-%m-%d"))
        .to_dict(orient="records")
    )


def get_events():

    events = pd.read_csv(
        DATA / "external" / "events.csv"
    )

    events["Date"] = pd.to_datetime(events["Date"])

    return (
        events.assign(Date=lambda d: d["Date"].dt.strftime("%Y-%m-%d"))
        .to_dict(orient="records")
    )


def get_dashboard_summary():

    df = pd.read_csv(
        DATA / "raw" / "BrentOilPrices.csv"
    )

    return {

        "average_price": round(df["Price"].mean(), 2),

        "highest_price": round(df["Price"].max(), 2),

        "lowest_price": round(df["Price"].min(), 2),

        "volatility": round(df["Price"].std(), 2),

        "total_events": 20,

    }


def get_change_point():

    """
    Temporary placeholder.

    Replace these values later with the outputs
    from Task 2.
    """

    return {

        "change_date": "2020-04-12",

        "before_mean": 42.5,

        "after_mean": 61.8,

        "percent_change": 45.41,

    }