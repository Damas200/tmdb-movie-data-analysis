"""
Orchestration Layer for TMDb Movie Data Pipeline.

Pipeline Flow:
    1. Extract   → TMDb API
    2. Transform → Cleaning + Feature Engineering
    3. Analyze   → KPI calculations
    4. Persist   → Save raw, processed, and KPI datasets

Design Principles:
    - Separation of Concerns
    - Clear pipeline stages
    - Minimal business logic here
    - Reusable modular architecture
    - Structured logging
"""

import os
import pandas as pd

from src.logger_config import setup_logger
from src.api_client import fetch_movie, fetch_credits
from src.data_cleaning import (
    flatten_json_columns,
    convert_data_types,
    filter_released_movies,
    enforce_minimum_data_quality
)
from src.feature_engineering import (
    add_financial_metrics,
    add_temporal_features,
    add_franchise_flag
)
from src.kpi_analysis import (
    financial_kpis,
    popularity_kpis,
    franchise_vs_standalone,
    most_successful_franchises,
    most_successful_directors
)

# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

MOVIE_IDS = [
    299534, 19995, 140607, 299536, 597, 135397,
    420818, 24428, 168259, 99861, 284054, 12445,
    181808, 330457, 351286, 109445, 321612, 260513
]

RAW_DATA_PATH = "data/raw/movies_raw.csv"
PROCESSED_DATA_PATH = "data/processed/movies_processed.csv"
KPI_DATA_PATH = "data/kpis"

logger = setup_logger()

# -------------------------------------------------------------------
# Extract
# -------------------------------------------------------------------

def extract_data(movie_ids):

    movies = []

    for movie_id in movie_ids:
        logger.info(f"[EXTRACT] Fetching movie ID {movie_id}")

        try:
            movie_data = fetch_movie(movie_id)
            credits_data = fetch_credits(movie_id)

            movie_data["cast"] = "|".join(
                [member["name"] for member in credits_data.get("cast", [])[:5]]
            )

            movie_data["director"] = next(
                (member["name"] for member in credits_data.get("crew", [])
                 if member.get("job") == "Director"),
                None
            )

            movies.append(movie_data)

        except Exception as e:
            logger.error(f"[ERROR] Failed processing movie {movie_id}: {e}")

    return pd.DataFrame(movies)

# -------------------------------------------------------------------
# Transform
# -------------------------------------------------------------------

def transform_data(df):

    logger.info("[TRANSFORM] Flattening JSON columns")
    df = flatten_json_columns(df)

    logger.info("[TRANSFORM] Converting data types")
    df = convert_data_types(df)

    logger.info("[TRANSFORM] Filtering released movies")
    df = filter_released_movies(df)

    logger.info("[TRANSFORM] Enforcing data quality")
    df = enforce_minimum_data_quality(df)

    logger.info("[TRANSFORM] Adding financial features")
    df = add_financial_metrics(df)

    logger.info("[TRANSFORM] Adding temporal features")
    df = add_temporal_features(df)

    logger.info("[TRANSFORM] Adding franchise flag")
    df = add_franchise_flag(df)

    return df

# -------------------------------------------------------------------
# Load (Raw + Processed)
# -------------------------------------------------------------------

def load_data(df_raw, df_processed):

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    df_raw.to_csv(RAW_DATA_PATH, index=False)
    df_processed.to_csv(PROCESSED_DATA_PATH, index=False)

    logger.info("[LOAD] Raw and processed datasets saved")

# -------------------------------------------------------------------
# KPI Persistence
# -------------------------------------------------------------------

def save_kpis(df_processed):

    os.makedirs(KPI_DATA_PATH, exist_ok=True)

    logger.info("[ANALYSIS] Computing financial KPIs")
    financial = financial_kpis(df_processed)

    logger.info("[ANALYSIS] Computing popularity KPIs")
    popularity = popularity_kpis(df_processed)

    logger.info("[ANALYSIS] Computing franchise comparison")
    franchise_comp = franchise_vs_standalone(df_processed)

    logger.info("[ANALYSIS] Computing most successful franchises")
    top_franchises = most_successful_franchises(df_processed)

    logger.info("[ANALYSIS] Computing most successful directors")
    top_directors = most_successful_directors(df_processed)

    # Save financial & popularity KPIs
    for name, df in {**financial, **popularity}.items():
        df.to_csv(f"{KPI_DATA_PATH}/{name}.csv", index=False)
        logger.info(f"[KPI SAVED] {name}.csv")

    # Save grouped KPIs
    franchise_comp.to_csv(f"{KPI_DATA_PATH}/franchise_vs_standalone.csv", index=False)
    top_franchises.to_csv(f"{KPI_DATA_PATH}/most_successful_franchises.csv", index=False)
    top_directors.to_csv(f"{KPI_DATA_PATH}/most_successful_directors.csv", index=False)

    logger.info("[KPI SAVED] Grouped KPI files saved")

# -------------------------------------------------------------------
# Pipeline Runner
# -------------------------------------------------------------------

def run_pipeline():

    logger.info("========== PIPELINE START ==========")

    df_raw = extract_data(MOVIE_IDS)
    df_processed = transform_data(df_raw)
    load_data(df_raw, df_processed)
    save_kpis(df_processed)

    logger.info("========== PIPELINE COMPLETE ==========")

# -------------------------------------------------------------------
# Entry Point
# -------------------------------------------------------------------

if __name__ == "__main__":
    run_pipeline()