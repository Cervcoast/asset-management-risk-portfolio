# utils/analytics.py
from __future__ import annotations

import numpy as np
import pandas as pd


def annualize_return(returns: pd.Series, periods_per_year: int = 252) -> float:
    returns = returns.dropna()
    if returns.empty:
        return float("nan")
    # For log returns, sum is log growth
    return float(np.exp(returns.mean() * periods_per_year) - 1)


def annualize_vol(returns: pd.Series, periods_per_year: int = 252) -> float:
    returns = returns.dropna()
    if returns.empty:
        return float("nan")
    return float(returns.std(ddof=1) * np.sqrt(periods_per_year))


def max_drawdown_from_returns(log_returns: pd.Series) -> float:
    """
    Assumes log returns. Computes max drawdown on cumulative equity curve.
    """
    r = log_returns.dropna()
    if r.empty:
        return float("nan")
    equity = np.exp(r.cumsum())
    peak = equity.cummax()
    dd = equity / peak - 1.0
    return float(dd.min())


def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    return returns.corr()
