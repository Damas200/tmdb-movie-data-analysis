
# TMDb Movie Data Analysis using Pandas and APIs

##  Project Overview

This project implements an end-to-end movie data analysis pipeline using **The Movie Database (TMDb) API**, **Python**, and **Pandas**.  
The objective is to extract real-world movie data, clean and transform it, compute key performance indicators (KPIs), perform advanced analysis, and communicate insights through visualizations.

The project follows **professional data engineering and analytics best practices**, with modular Python scripts and a Jupyter Notebook used only for orchestration.

---

##  Project Objectives

- Fetch movie metadata and credits using the TMDb API  
- Clean and preprocess nested and inconsistent data  
- Perform exploratory data analysis (EDA)  
- Engineer financial and popularity KPIs  
- Rank and filter movies using advanced criteria  
- Analyze franchise and director performance  
- Visualize trends and extract actionable insights  

---

## Project Structure

```text

tmdb-movie-data-analysis/
│
├── functions/
│   ├── api.py              # TMDb API data extraction
│   ├── credits.py          # Cast, director, and crew extraction
│   ├── cleaning.py         # Data cleaning and preprocessing
│   ├── features.py         # KPI and feature engineering
│   ├── analysis.py         # Ranking, filtering, and aggregated analysis
│   └── visualization.py   # Matplotlib visualizations
│
├── tmdb_movie_analysis.ipynb   # Main Jupyter Notebook (orchestration only)
├── README.md
└── .gitignore
```

---

##  API Configuration

This project uses the **TMDb API**.

1. Create an account at https://www.themoviedb.org/
2. Generate an API key
3. Insert your API key inside the notebook:

```python
API_KEY = "YOUR_API_KEY_HERE"
````


##  Workflow Summary

### Step 1: API Data Extraction

* Fetch movie metadata using predefined movie IDs
* Fetch cast, director, and crew information using the credits endpoint

### Step 2: Data Cleaning & Preprocessing

* Drop irrelevant columns
* Normalize nested JSON fields
* Handle missing, zero, and unrealistic values
* Convert budgets and revenues to million USD
* Filter released movies only

### Step 3: Feature Engineering & KPI Analysis

* Compute:

  * Budget (Million USD)
  * Revenue (Million USD)
  * Profit
  * Return on Investment (ROI)
* Rank movies by:

  * Revenue
  * Budget
  * Profit
  * ROI (budget ≥ 10M)
  * Popularity
  * Ratings (vote count ≥ 10)
* Perform advanced filtering:

  * Science Fiction & Action movies starring Bruce Willis
  * Movies starring Uma Thurman and directed by Quentin Tarantino
* Analyze franchise vs standalone performance
* Identify top franchises and directors

### Step 4: Data Visualization

* Revenue vs Budget trends
* ROI distribution by genre
* Popularity vs Rating
* Yearly box office revenue trends
* Franchise vs Standalone comparison

---

##  Visualization Insights & Interpretation

### Revenue vs Budget

* Higher budgets generally lead to higher revenues.
* However, large budgets do not guarantee success.
* Several mid-budget movies achieve strong revenues.

### Top Genres by Mean ROI

* Genres such as **Fantasy, Comedy, and Romance** show the highest average ROI.
* High-budget genres like **Action and Science Fiction** have lower average ROI.
* Moderate-budget genres tend to be more cost-efficient.

### Popularity vs Rating

* Popularity and rating are weakly correlated.
* Some highly popular movies receive average ratings.
* Less popular movies can still achieve high ratings.

### Yearly Box Office Revenue Trends

* Revenue varies significantly across years.
* Peaks correspond to blockbuster releases.
* The industry is driven by hit movies rather than steady growth.

### Franchise vs Standalone Movies

* Franchise movies generate slightly higher average revenue.
* Standalone movies remain competitive and can achieve strong performance.
* Franchise status alone does not guarantee success.

---

##  Key Takeaways

* Movie success is multi-dimensional.
* Budget, genre, popularity, and franchise status all matter.
* ROI often favors lower-to-mid budget genres.
* Popularity does not always reflect audience satisfaction.

---

## Technologies Used

* Python 3
* Pandas
* NumPy
* Requests
* Matplotlib
* Jupyter Notebook / Google Colab

---

##  How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Damas200/tmdb-movie-data-analysis.git
```

2. Open `tmdb_movie_analysis.ipynb` in Jupyter Notebook or Google Colab

3. Install required packages if needed:

```bash
pip install pandas numpy requests matplotlib
```

4. Run the notebook cells from top to bottom

