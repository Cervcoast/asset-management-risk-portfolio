# utils/data.py
from __future__ import annotations

import os
import pandas as pd
import numpy as np
import yfinance as yf


def ensure_dirs(paths: list[str]) -> None:
    for p in paths:
        os.makedirs(p, exist_ok=True)


def download_prices(
    tickers: list[str],
    start: str,
    end: str | None,
    field: str = "Adj Close",
) -> pd.DataFrame:
    """
    Downloads daily prices from Yahoo Finance.
    Returns a wide DataFrame indexed by date with columns=tickers.
    """
    df = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        auto_adjust=False,
        progress=False,
        group_by="column",
        threads=True,
    )

    # yfinance returns MultiIndex columns when multiple tickers
    if isinstance(df.columns, pd.MultiIndex):
        if field not in df.columns.levels[0]:
            raise ValueError(f"Field '{field}' not found in downloaded data.")
        prices = df[field].copy()
    else:
        # single ticker
        prices = df[[field]].copy()
        prices.columns = tickers[:1]

    prices.index = pd.to_datetime(prices.index)
    prices = prices.sort_index()
    return prices


def compute_returns(prices: pd.DataFrame, kind: str = "log") -> pd.DataFrame:
    prices = prices.astype(float)
    if kind == "log":
        rets = np.log(prices / prices.shift(1))
    elif kind == "simple":
        rets = prices.pct_change()
    else:
        raise ValueError("kind must be 'log' or 'simple'")
    return rets.dropna(how="all")


def coverage_filter(prices: pd.DataFrame, min_coverage: float = 0.98) -> tuple[pd.DataFrame, pd.Series]:
    """
    Drops tickers with insufficient coverage.
    Coverage is share of non-NaN values across dates.
    """
    coverage = prices.notna().mean(axis=0).sort_values(ascending=False)
    keep = coverage[coverage >= min_coverage].index.tolist()
    filtered = prices[keep].copy()
    return filtered, coverage


def align_and_clean(prices: pd.DataFrame) -> pd.DataFrame:
    """
    - Drops duplicate dates
    - Ensures business-day frequency by keeping observed trading days
    - Forward-fill short gaps per asset is generally NOT ideal for returns; we keep NaNs
    """
    prices = prices[~prices.index.duplicated(keep="first")].copy()
    prices = prices.sort_index()
    return prices
