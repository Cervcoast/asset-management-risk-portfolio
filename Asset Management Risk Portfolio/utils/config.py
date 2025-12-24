# utils/config.py
from __future__ import annotations

ASSET_UNIVERSE = {
    # Core Macro / Allocation ETFs
    "SPY": "US Equity",
    "QQQ": "US Growth",
    "IWM": "US Small Cap",
    "DIA": "US Dow",
    "EFA": "Developed Intl",
    "EEM": "Emerging Mkts",
    "VNQ": "US REITs",
    "GLD": "Gold",
    "DBC": "Broad Commodities",
    "TLT": "US Long Treasuries",
    "IEF": "US Intermediate Treasuries",
    "SHY": "US Short Treasuries",
    "AGG": "US Aggregate Bonds",
    "HYG": "High Yield Credit",
    "LQD": "Investment Grade Credit",
    "TIP": "TIPS",

    # Sector ETFs (Risk Decomposition)
    "XLK": "Tech",
    "XLF": "Financials",
    "XLE": "Energy",
    "XLV": "Healthcare",
    "XLY": "Consumer Disc",
    "XLP": "Consumer Staples",
    "XLI": "Industrials",
    "XLB": "Materials",
    "XLU": "Utilities",

    # Large-cap Equities (Risk Drivers)
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "NVDA": "NVIDIA",
    "AMZN": "Amazon",
    "META": "Meta",
    "GOOGL": "Alphabet",
    "TSLA": "Tesla",
    "BRK-B": "Berkshire",
    "JPM": "JPMorgan",
    "GS": "Goldman",
    "BAC": "Bank of America",
    "UNH": "UnitedHealth",
    "JNJ": "Johnson & Johnson",
    "PFE": "Pfizer",
    "XOM": "Exxon",
    "CVX": "Chevron",
    "COST": "Costco",
    "WMT": "Walmart",
    "HD": "Home Depot",
    "KO": "Coca-Cola",
}

START_DATE = "2014-01-01"
END_DATE = None  # None => up to latest available
PRICE_FIELD = "Adj Close"
MIN_COVERAGE = 0.98  # keep tickers with >=98% of dates present
RETURN_KIND = "log"  # "log" or "simple"

RAW_PRICES_PARQUET = "data/raw/prices.parquet"
PROCESSED_RETURNS_PARQUET = "data/processed/returns.parquet"
