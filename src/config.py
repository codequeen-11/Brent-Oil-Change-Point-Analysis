"""
Project configuration settings.
"""

from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

# Reports
REPORT_DIR = ROOT_DIR / "reports"
FIGURE_DIR = REPORT_DIR / "figures"

# Dataset
BRENT_DATA = RAW_DATA_DIR / "BrentOilPrices.csv"
EVENT_DATA = EXTERNAL_DATA_DIR / "events.csv"