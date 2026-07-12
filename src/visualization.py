"""
Visualization functions.
"""

import matplotlib.pyplot as plt
from pathlib import Path

def save_figure(filename: str):
    figures_dir = Path("reports/figures")
    figures_dir.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        figures_dir / filename,
        dpi=300,
        bbox_inches="tight"
    )

def plot_price(df):

    plt.figure(figsize=(15,6))

    plt.plot(df["Date"], df["Price"])

    plt.title("Historical Brent Oil Prices")

    plt.xlabel("Date")

    plt.ylabel("Price (USD/Barrel)")

    plt.grid(True)

    plt.tight_layout()

    # plt.show()
    save_figure("price_trend.png")
    plt.show()


def plot_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["Price"], bins=30)

    plt.title("Distribution of Brent Oil Prices")

    plt.xlabel("Price")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.show()


def plot_boxplot(df):

    plt.figure(figsize=(5,6))

    plt.boxplot(df["Price"])

    plt.title("Boxplot of Brent Oil Prices")

    plt.tight_layout()

    plt.show()


def plot_rolling_statistics(df, rolling_mean, rolling_std):

    plt.figure(figsize=(15,6))

    plt.plot(df["Date"], df["Price"], label="Price")

    plt.plot(df["Date"], rolling_mean, label="Rolling Mean")

    plt.plot(df["Date"], rolling_std, label="Rolling Std")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.show()


def plot_log_returns(df):

    plt.figure(figsize=(15,5))

    plt.plot(df["Date"], df["Log_Return"])

    plt.title("Log Returns")

    plt.grid(True)

    plt.tight_layout()

    plt.show()