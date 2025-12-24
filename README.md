# 📊 Asset Management Risk Portfolio  
**Multi-Asset Portfolio Construction, Risk Attribution & Stress Testing**

---

## Overview

This project implements an **institutional-style portfolio risk management framework** used by asset managers to construct, monitor, and stress-test multi-asset portfolios across market regimes.

Rather than focusing purely on return optimization, the framework emphasizes:

- Risk ownership and concentration  
- Drawdown control  
- Tail-risk behavior  
- Regime sensitivity  
- Ongoing risk monitoring  

The analysis is performed on a **30–50 asset universe** spanning equities, rates, credit, commodities, and sectors, using daily data and professional risk diagnostics.

---

## Asset Universe

The portfolio universe includes:

**Core Equity ETFs**
- SPY, QQQ, IWM, EFA, EEM  

**Fixed Income & Credit**
- AGG, TLT, IEF, HYG, LQD, TIP  

**Real Assets**
- GLD, VNQ, DBC  

**Sector ETFs**
- XLK, XLF, XLE, XLV, XLU, etc.  

**Large-Cap Equities**
- AAPL, MSFT, NVDA, AMZN, META  
- JPM, GS, XOM  
- UNH, COST, WMT, and others  

Assets are filtered for data completeness and aligned to a common trading window to ensure consistency.

---

## Portfolio Construction Framework

### 1. Baseline Portfolios (Controls)

Two benchmark portfolios are constructed:

- **Equal-Weight Portfolio**
- **Mean-Variance Optimized (MVO) Portfolio**
  - Long-only  
  - Fully invested  
  - Position size caps to limit concentration  

These portfolios serve as **controls** for evaluating diversification, concentration risk, and drawdown behavior.

---

### 2. Risk Parity Portfolio (Core Strategy)

A **risk-parity portfolio** is constructed such that each asset contributes equally to total portfolio volatility.

**Key features**
- Allocation based on **risk contribution**, not capital weight  
- Reduced exposure to correlation spikes  
- Improved drawdown stability across regimes  

This portfolio serves as the primary candidate for risk-controlled allocation.

---

## Risk Attribution

Risk attribution is performed using:

- Marginal Risk Contribution (MRC)  
- Component Risk Contribution (CRC)  
- Percentage of Total Risk by Asset  

This analysis answers:
- Which assets truly drive portfolio volatility?  
- How concentrated is portfolio risk?  
- How does risk ownership change over time?  

Rolling attribution highlights **regime-dependent concentration**, particularly during market stress.

---

## Stress Testing & Scenario Analysis

### Historical Stress Replay

Portfolios are evaluated during major market stress periods:

- Global Financial Crisis (2008–2009)  
- COVID-19 Crash (2020)  
- Inflation & Rate Shock (2022)  

**Metrics include**
- Cumulative loss  
- Maximum drawdown  
- Worst single-day and multi-day losses  
- Recovery time (where applicable)  
- Asset-level loss attribution  

---

### Macro Scenario Shocks

Custom macro shocks are applied to assess vulnerability to:

- Equity sell-offs  
- Rate hikes / duration shocks  
- Credit spread widening  

Each scenario reports:
- Portfolio-level impact  
- Top loss contributors  
- Cross-asset diversification behavior  

---

## Risk Monitoring & Alerts

A rolling risk dashboard is implemented to replicate an **internal risk monitoring system**, including:

- Rolling annualized volatility  
- Drawdown tracking  
- Historical VaR & CVaR  
- VaR breach diagnostics  
- Correlation spike detection  
- Simple “red-flag” alert rules  

This enables **ongoing portfolio oversight**, not just static analysis.

---

## Key Insights

- Mean-variance portfolios often reduce volatility but **concentrate risk in a few assets**  
- Risk parity produces **more balanced risk ownership**, particularly during stress  
- Diversification frequently breaks down during crises — **correlation monitoring is critical**  
- Risk management is an **ongoing process**, not a one-time optimization  

---

## Repository Structure
asset-management-risk-portfolio/
├── notebooks/
│ ├── 01_asset_universe.ipynb
│ ├── 02_baseline_portfolios.ipynb
│ ├── 03_risk_parity_portfolio.ipynb
│ ├── 04_risk_attribution.ipynb
│ ├── 05_stress_testing.ipynb
│ └── 06_rolling_risk_monitoring.ipynb
│
├── utils/
│ ├── config.py
│ ├── data.py
│ └── analytics.py
│
├── data/
│ ├── raw/
│ └── processed/
│
└── README.md


---

## Tools & Methods

- **Python:** pandas, numpy, scipy, matplotlib  
- **Optimization:** constrained nonlinear optimization  
- **Risk Metrics:** volatility, drawdown, VaR, CVaR  
- **Techniques:** risk parity, attribution, stress testing, rolling analytics  

---

## Intended Audience

This project is designed for:
- Asset Management  
- Portfolio Risk  
- Investment Analytics  
- Quantitative Research  
- Buy-Side Risk & Strategy Teams  

---

## Disclaimer

This project is for **educational and analytical purposes only** and does not constitute investment advice.

