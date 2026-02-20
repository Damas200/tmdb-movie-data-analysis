"""
Responsibility:
    This module contains all visualization logic for the
    TMDb Movie Data Analysis project.

Design Principles:
    - Separation of Concerns (no cleaning or KPI logic)
    - Pure visualization functions
    - Defensive validation
    - Consistent styling
    - Report-ready figures

"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Global Plot Configuration
# -------------------------------------------------------------------

# Set consistent professional style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titleweight"] = "bold"


# Revenue vs Budget Scatter (with Trend Line)
# -------------------------------------------------------------------

def plot_revenue_vs_budget(df: pd.DataFrame) -> None:
    """
    Scatter plot of Budget vs Revenue with regression trendline.

    Insight:
        Evaluates correlation between production investment
        and box office performance.
    """

    required_cols = ["budget_musd", "revenue_musd"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    plt.figure()
    sns.regplot(
        data=df,
        x="budget_musd",
        y="revenue_musd",
        scatter_kws={"alpha": 0.7}
    )

    plt.title("Revenue vs Budget (Million USD)")
    plt.xlabel("Budget (Million USD)")
    plt.ylabel("Revenue (Million USD)")
    plt.tight_layout()
    plt.show()


# ROI Distribution by Genre
# -------------------------------------------------------------------

def plot_roi_by_genre(df: pd.DataFrame) -> None:
    """
    Boxplot showing ROI distribution by genre.

    Insight:
        Identifies which genres produce higher variability
        and stronger investment returns.
    """

    required_cols = ["genres", "roi"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Explode multi-genre entries
    temp = df.copy()
    temp = temp.dropna(subset=["genres", "roi"])
    temp = temp.assign(genres=temp["genres"].str.split("|"))
    temp = temp.explode("genres")

    plt.figure()
    sns.boxplot(data=temp, x="genres", y="roi")

    plt.xticks(rotation=45)
    plt.title("ROI Distribution by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Return on Investment (ROI)")
    plt.tight_layout()
    plt.show()


# Popularity vs Rating Scatter
# -------------------------------------------------------------------

def plot_popularity_vs_rating(df: pd.DataFrame) -> None:
    """
    Scatter plot of Popularity vs Vote Average.

    Insight:
        Examines whether audience popularity aligns with
        critical ratings.
    """

    required_cols = ["popularity", "vote_average"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    plt.figure()
    sns.scatterplot(
        data=df,
        x="vote_average",
        y="popularity",
        alpha=0.7
    )

    plt.title("Popularity vs Vote Average")
    plt.xlabel("Vote Average")
    plt.ylabel("Popularity Score")
    plt.tight_layout()
    plt.show()


# Yearly Revenue Trend
# -------------------------------------------------------------------

def plot_yearly_revenue_trend(df: pd.DataFrame) -> None:
    """
    Line plot showing revenue trends over time.

    Insight:
        Evaluates macro-level box office evolution.
    """

    if "release_year" not in df.columns:
        raise ValueError("release_year column missing")

    yearly = (
        df.groupby("release_year")["revenue_musd"]
        .sum()
        .reset_index()
        .sort_values("release_year")
    )

    plt.figure()
    sns.lineplot(data=yearly, x="release_year", y="revenue_musd")

    plt.title("Total Revenue by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Total Revenue (Million USD)")
    plt.tight_layout()
    plt.show()


# Franchise vs Standalone Comparison
# -------------------------------------------------------------------

def plot_franchise_comparison(df: pd.DataFrame) -> None:
    """
    Compare mean revenue between franchise and standalone films.

    Insight:
        Visual confirmation of franchise dominance hypothesis.
    """

    if "is_franchise" not in df.columns:
        raise ValueError("is_franchise column missing")

    comparison = (
        df.groupby("is_franchise")["revenue_musd"]
        .mean()
        .reset_index()
    )

    plt.figure()
    sns.barplot(data=comparison, x="is_franchise", y="revenue_musd")

    plt.title("Average Revenue: Franchise vs Standalone")
    plt.xlabel("Is Franchise")
    plt.ylabel("Mean Revenue (Million USD)")
    plt.tight_layout()
    plt.show()