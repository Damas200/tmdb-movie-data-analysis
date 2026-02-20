"""
Responsibility:
    This module implements analytical KPIs and ranking logic
    for TMDb movie performance analysis.

Design Principles:
    - Separation of Concerns: No API or cleaning logic.
    - Reusable ranking utilities.
    - Defensive validation.
    - Business-oriented aggregation logic.
    - Production-ready analytics layer.

"""

import pandas as pd
import numpy as np
from typing import Optional

# Generic Ranking Utility
# -------------------------------------------------------------------

def rank_movies(
    df: pd.DataFrame,
    column: str,
    ascending: bool = False,
    min_vote_count: Optional[int] = None,
    min_budget: Optional[float] = None,
    top_n: int = 10
) -> pd.DataFrame:
    """
    Generic reusable ranking function.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset containing movie data.
    column : str
        Column to rank by.
    ascending : bool
        Sorting direction.
    min_vote_count : Optional[int]
        Filter for minimum vote_count.
    min_budget : Optional[float]
        Filter for minimum budget_musd.
    top_n : int
        Number of top rows to return.

    Returns
    -------
    pd.DataFrame
        Ranked subset of movies.
    """

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")

    temp = df.copy()

    # Apply conditional filters
    if min_vote_count is not None and "vote_count" in temp.columns:
        temp = temp[temp["vote_count"] >= min_vote_count]

    if min_budget is not None and "budget_musd" in temp.columns:
        temp = temp[temp["budget_musd"] >= min_budget]

    # Remove NaN in ranking column
    temp = temp.dropna(subset=[column])

    return temp.sort_values(column, ascending=ascending).head(top_n)


# Financial KPI Rankings
# -------------------------------------------------------------------

def financial_kpis(df: pd.DataFrame) -> dict:
    """
    Compute key financial ranking tables.

    Returns
    -------
    dict
        Dictionary of KPI DataFrames.
    """

    return {
        "top_revenue": rank_movies(df, "revenue_musd"),
        "top_budget": rank_movies(df, "budget_musd"),
        "top_profit": rank_movies(df, "profit_musd"),
        "lowest_profit": rank_movies(df, "profit_musd", ascending=True),
        "top_roi": rank_movies(df, "roi", min_budget=10),
        "lowest_roi": rank_movies(df, "roi", ascending=True, min_budget=10)
    }


# Popularity & Rating KPIs
# -------------------------------------------------------------------

def popularity_kpis(df: pd.DataFrame) -> dict:
    """
    Compute popularity and rating-based rankings.
    """

    return {
        "most_voted": rank_movies(df, "vote_count"),
        "highest_rated": rank_movies(df, "vote_average", min_vote_count=10),
        "lowest_rated": rank_movies(df, "vote_average", ascending=True, min_vote_count=10),
        "most_popular": rank_movies(df, "popularity")
    }


# Advanced Filtering Queries
# -------------------------------------------------------------------

def filter_sci_fi_action_bruce_willis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Best-rated Sci-Fi + Action movies with Bruce Willis.
    """

    required_cols = ["genres", "cast", "vote_average"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    return (
        df[
            df["genres"].str.contains("Science Fiction", na=False) &
            df["genres"].str.contains("Action", na=False) &
            df["cast"].str.contains("Bruce Willis", na=False)
        ]
        .sort_values("vote_average", ascending=False)
    )


def filter_uma_thurman_tarantino(df: pd.DataFrame) -> pd.DataFrame:
    """
    Movies starring Uma Thurman and directed by Quentin Tarantino.
    """

    required_cols = ["cast", "director", "runtime"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    return (
        df[
            df["cast"].str.contains("Uma Thurman", na=False) &
            (df["director"] == "Quentin Tarantino")
        ]
        .sort_values("runtime")
    )


# Franchise vs Standalone Analysis
# -------------------------------------------------------------------

def franchise_vs_standalone(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare average performance of franchise vs standalone films.
    """

    if "is_franchise" not in df.columns:
        raise ValueError("is_franchise column missing")

    return (
        df.groupby("is_franchise")
        .agg(
            mean_revenue=("revenue_musd", "mean"),
            median_roi=("roi", "median"),
            mean_budget=("budget_musd", "mean"),
            mean_popularity=("popularity", "mean"),
            mean_rating=("vote_average", "mean")
        )
        .reset_index()
    )


# Most Successful Franchises
# -------------------------------------------------------------------

def most_successful_franchises(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rank franchises by total revenue.
    """

    if "belongs_to_collection" not in df.columns:
        raise ValueError("belongs_to_collection column missing")

    return (
        df[df["belongs_to_collection"].notna()]
        .groupby("belongs_to_collection")
        .agg(
            total_movies=("title", "count"),
            total_budget=("budget_musd", "sum"),
            total_revenue=("revenue_musd", "sum"),
            mean_revenue=("revenue_musd", "mean"),
            mean_rating=("vote_average", "mean")
        )
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )


# Most Successful Directors
# -------------------------------------------------------------------

def most_successful_directors(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rank directors by total revenue and performance.
    """

    if "director" not in df.columns:
        raise ValueError("director column missing")

    return (
        df.groupby("director")
        .agg(
            total_movies=("title", "count"),
            total_revenue=("revenue_musd", "sum"),
            mean_rating=("vote_average", "mean"),
            mean_roi=("roi", "mean")
        )
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )