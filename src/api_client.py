"""
Responsibility:
    This module handles all communication with the TMDb REST API.

Design Principles:
    - Separation of Concerns: No data cleaning or business logic here.
    - Single Responsibility: Only API interaction.
    - Reusable & testable.
    - Secure configuration using environment variables.
"""

import os
import requests
from dotenv import load_dotenv


# Configuration Layer
# -------------------------------------------------------------------

# Load environment variables from .env file
# This prevents hardcoding sensitive credentials inside source code.
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

# Base URL for all TMDb API endpoints
BASE_URL = "https://api.themoviedb.org/3"


# Validation

# Fail early if API key is missing
if API_KEY is None:
    raise ValueError(
        "TMDB_API_KEY not found. Please define it inside the .env file."
    )


# Core API Functions
# -------------------------------------------------------------------

def fetch_movie(movie_id: int) -> dict:
    """
    Fetch detailed metadata for a given movie.

    Parameters
    ----------
    movie_id : int
        Unique TMDb movie ID.

    Returns
    -------
    dict
        JSON response containing movie metadata.

    Raises
    ------
    requests.HTTPError
        If API request fails (e.g., invalid ID or network issue).
    """

    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        # Logging could be added here in production
        print(f"[API ERROR] Failed to fetch movie {movie_id}: {e}")
        raise


def fetch_credits(movie_id: int) -> dict:
    """
    Fetch cast and crew information for a given movie.

    Parameters
    ----------
    movie_id : int
        Unique TMDb movie ID.

    Returns
    -------
    dict
        JSON response containing cast and crew details.
    """

    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {"api_key": API_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"[API ERROR] Failed to fetch credits for movie {movie_id}: {e}")
        raise