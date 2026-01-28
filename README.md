# TMDb Movie Data Analysis using Pandas and APIs

## Project Overview

This project builds an end-to-end movie data analysis pipeline using the TMDb API. It involves fetching movie data, cleaning and preprocessing it, computing key performance indicators such as profit and ROI, and visualizing trends to gain insights into movie performance.

---

## Project Objectives

- Fetch movie data programmatically from the TMDb API
- Clean and preprocess raw JSON data into a structured format
- Perform exploratory data analysis (EDA)
- Implement key performance indicators (KPIs)
- Analyze movie performance by budget, revenue, ROI, genre, popularity, and franchise status
- Visualize trends and relationships using Matplotlib

---

##  Tools & Technologies

- **Python 3**
- **Pandas** – data manipulation and analysis
- **NumPy** – numerical computations
- **Requests** – API communication
- **Matplotlib** – data visualization
- **Jupyter Notebook**
- **TMDb API**

---



## Project Workflow

### Step 1: API Data Extraction
- Fetch movie details using predefined TMDb movie IDs
- Store API responses in a Pandas DataFrame

### Step 2: Data Cleaning & Preprocessing
- Drop irrelevant columns
- Extract nested JSON fields (genres, production companies, languages, etc.)
- Handle missing and unrealistic values
- Convert financial values to million USD
- Filter only released movies

### Step 3: KPI Implementation & Analysis
- Compute profit and return on investment (ROI)
- Rank movies by revenue, budget, profit, ROI, popularity, and ratings
- Perform advanced filtering (genre, actor, director-based queries)
- Analyze franchise vs standalone movie performance
- Identify top-performing genres, franchises, and directors

### Step 4: Data Visualization
- Revenue vs budget trends
- ROI distribution by genre
- Popularity vs rating relationship
- Yearly box office revenue trends
- Franchise vs standalone revenue comparison

---

## Key Insights 

- Higher budgets generally lead to higher revenues, but not always higher profitability
- Medium-budget movies can achieve strong ROI
- Fantasy, Comedy, and Romance genres show high average ROI
- Popularity and user ratings have a weak correlation
- Standalone movies can perform as well as, or better than, franchise movies in terms of mean revenue

---

