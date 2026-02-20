"""
Responsibility:
    This module creates derived analytical features 
    from cleaned TMDb movie data.

Design Principles:
    - Separation of Concerns: No API calls or cleaning logic.
    - Pure transformations (no in-place mutation).
    - Financial metrics computed safely.
    - Explicit handling of missing values.

"""

import pandas as pd
import numpy as np

# Financial Feature Engineering
# -------------------------------------------------------------------

def add_financial_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create financial performance metrics for analysis.

    New Features:
        - budget_musd      : Budget in million USD
        - revenue_musd     : Revenue in million USD
        - profit_musd      : Revenue - Budget
        - roi              : Return on Investment (Revenue / Budget)

    Assumptions:
        - Budget and revenue are in USD.
        - Zero values have already been converted to NaN in cleaning layer.
        - ROI is only computed when budget > 0.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned movie dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with added financial metrics.
    """

    df = df.copy()

    required_columns = ["budget", "revenue"]

    # Validate required columns exist
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert to million USD for readability
    df["budget_musd"] = df["budget"] / 1_000_000
    df["revenue_musd"] = df["revenue"] / 1_000_000

    # Profit calculation
    df["profit_musd"] = df["revenue_musd"] - df["budget_musd"]

    # Safe ROI calculation (avoid division by zero)
    df["roi"] = np.where(
        df["budget_musd"] > 0,
        df["revenue_musd"] / df["budget_musd"],
        np.nan
    )

    return df

# Cast & Crew Feature Engineering
# -------------------------------------------------------------------

def add_cast_crew_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add cast and crew size metrics if not already computed.

    Ensures:
        - cast_size column exists
        - crew_size column exists

    Useful for analyzing production scale vs performance.
    """

    df = df.copy()

    if "cast" in df.columns and "cast_size" not in df.columns:
        df["cast_size"] = df["cast"].apply(
            lambda x: len(x.split("|")) if isinstance(x, str) else np.nan
        )

    if "crew" in df.columns and "crew_size" not in df.columns:
        df["crew_size"] = df["crew"].apply(
            lambda x: len(x) if isinstance(x, list) else np.nan
        )

    return df

# Temporal Feature Engineering
# -------------------------------------------------------------------

def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract time-based features from release_date.

    New Features:
        - release_year
        - release_month
        - release_decade

    Enables trend analysis over time.
    """

    df = df.copy()

    if "release_date" not in df.columns:
        raise ValueError("release_date column not found")

    df["release_year"] = df["release_date"].dt.year
    df["release_month"] = df["release_date"].dt.month
    df["release_decade"] = (df["release_year"] // 10) * 10

    return df

# Franchise Indicator
# -------------------------------------------------------------------

def add_franchise_flag(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary indicator for franchise membership.

    New Feature:
        - is_franchise (True/False)

    This allows grouped comparison between:
        Franchise vs Standalone films.
    """

    df = df.copy()

    if "belongs_to_collection" not in df.columns:
        raise ValueError("belongs_to_collection column missing")

    df["is_franchise"] = df["belongs_to_collection"].notna()

    return df