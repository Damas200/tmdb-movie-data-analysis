"""
Responsibility:
    This module transforms raw TMDb JSON data into a 
    structured, analysis-ready Pandas DataFrame.

Design Principles:
    - Separation of Concerns: No API calls or analytics logic.
    - Pure transformations (functions return new DataFrames).
    - Defensive programming for missing / malformed data.
    - Reusable and testable functions.

"""

import pandas as pd
import numpy as np
from typing import List


# Utility Functions
# -------------------------------------------------------------------

def _extract_pipe_separated_names(obj: List[dict]) -> str:
    """
    Convert a list of dictionaries (e.g., genres, companies)
    into a pipe-separated string of names.

    Example:
        [{"id": 1, "name": "Action"}, {"id": 2, "name": "Sci-Fi"}]
        -> "Action|Sci-Fi"

    Returns NaN if input is invalid or empty.
    """

    if isinstance(obj, list) and len(obj) > 0:
        return "|".join(item.get("name", "") for item in obj if "name" in item)
    return np.nan


# JSON Flattening Layer
# -------------------------------------------------------------------

def flatten_json_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flatten nested JSON columns into analysis-friendly format.

    Transformations:
        - genres → pipe-separated string
        - production_companies → pipe-separated string
        - production_countries → pipe-separated string
        - spoken_languages → pipe-separated string
        - belongs_to_collection → collection name only

    Parameters
    ----------
    df : pd.DataFrame
        Raw movie metadata DataFrame.

    Returns
    -------
    pd.DataFrame
        Transformed DataFrame with flattened columns.
    """

    df = df.copy()  # avoid modifying original reference

    json_columns = [
        "genres",
        "production_companies",
        "production_countries",
        "spoken_languages"
    ]

    for col in json_columns:
        if col in df.columns:
            df[col] = df[col].apply(_extract_pipe_separated_names)

    # Extract collection name if available
    if "belongs_to_collection" in df.columns:
        df["belongs_to_collection"] = df["belongs_to_collection"].apply(
            lambda x: x["name"] if isinstance(x, dict) else np.nan
        )

    return df

# Type Conversion & Data Integrity Layer
# -------------------------------------------------------------------

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert relevant columns to appropriate data types.

    - Numeric financial columns → float
    - release_date → datetime
    - Replace 0 values in budget/revenue/runtime with NaN

    This prevents misleading financial analysis caused by zero placeholders.
    """

    df = df.copy()

    numeric_columns = [
        "budget",
        "revenue",
        "runtime",
        "popularity",
        "vote_count",
        "vote_average"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

            # Replace zero placeholders with NaN
            if col in ["budget", "revenue", "runtime"]:
                df.loc[df[col] == 0, col] = np.nan

    # Convert release_date safely
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(
            df["release_date"],
            errors="coerce"
        )

    return df


# Data Quality Filtering Layer
# -------------------------------------------------------------------

def filter_released_movies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only movies with status = 'Released'.

    Removes the status column afterward since it is no longer needed.
    """

    df = df.copy()

    if "status" in df.columns:
        df = df[df["status"] == "Released"]
        df = df.drop(columns="status")

    return df


def enforce_minimum_data_quality(df: pd.DataFrame, min_non_null: int = 10) -> pd.DataFrame:
    """
    Ensure each row has at least a minimum number of non-null fields.

    This prevents incomplete API records from affecting analysis.

    Parameters
    ----------
    min_non_null : int
        Minimum required non-null columns per row.
    """

    df = df.copy()
    # Drop duplicates based on stable identifier columns
    if "id" in df.columns:
        df = df.drop_duplicates(subset=["id"])
    else:
        df = df.drop_duplicates()
    # Drop rows missing critical identifiers
    df = df.dropna(subset=["id", "title"])

    # Enforce minimum data completeness
    df = df[df.count(axis=1) >= min_non_null]

    return df