#  KPI Summary Report

## TMDb Movie Performance Analysis

This document summarizes the key performance indicators (KPIs) generated from the processed TMDb dataset. All KPI tables were programmatically exported from the ETL pipeline and stored under `data/kpis/`.

---

# 1️. Financial Performance KPIs

##  Top 10 Highest Revenue

Source: `data/kpis/top_revenue.csv`

These films generated the highest total box office revenue (Million USD).
The ranking highlights the dominance of large-scale global blockbusters and franchise-driven productions.

**Insight:**
High-revenue films are typically characterized by strong franchise branding, international appeal, and substantial production budgets.

---

##  Top 10 Highest Budget

Source: `data/kpis/top_budget.csv`

This ranking identifies the most capital-intensive productions.

**Insight:**
Large budgets are strongly associated with visual effects-heavy genres such as Action, Fantasy, and Science Fiction. However, high budget alone does not guarantee maximum profitability.

---

##  Top 10 Highest Profit

Source: `data/kpis/top_profit.csv`

Profit is calculated as:

> Profit = Revenue − Budget

**Insight:**
Some films achieve extraordinary profitability due to strong audience reception and global market expansion, reinforcing the scalability of blockbuster models.

---

##  Lowest Profit

Source: `data/kpis/lowest_profit.csv`

These films generated comparatively weaker profit margins.

**Insight:**
Lower profitability may result from high production costs, weaker audience reception, or competitive release timing.

---

##  Top ROI (Budget ≥ 10M USD)

Source: `data/kpis/top_roi.csv`

Return on Investment (ROI):

> ROI = Revenue / Budget

**Insight:**
High ROI films demonstrate efficient capital utilization. Moderate-budget films sometimes outperform mega-budget productions in terms of investment efficiency.

---

## Lowest ROI (Budget ≥ 10M USD)

Source: `data/kpis/lowest_roi.csv`

**Insight:**
Low ROI films indicate inefficient capital deployment, where large production costs were not proportionally matched by revenue.

---

# 2️. Audience & Popularity KPIs

##  Most Voted Movies

Source: `data/kpis/most_voted.csv`

This ranking reflects audience engagement volume.

**Insight:**
Highly voted films often belong to globally recognized franchises with broad demographic reach.

---

##  Highest Rated Movies (Vote Count ≥ 10)

Source: `data/kpis/highest_rated.csv`

These films achieved the strongest average audience ratings.

**Insight:**
Critical success does not always align perfectly with revenue performance, suggesting different dynamics between artistic quality and commercial success.

---

##  Lowest Rated Movies

Source: `data/kpis/lowest_rated.csv`

**Insight:**
Lower ratings may indicate audience dissatisfaction despite possible commercial performance.

---

##  Most Popular Movies

Source: `data/kpis/most_popular.csv`

Popularity reflects TMDb engagement metrics rather than direct financial success.

**Insight:**
Popularity is influenced by marketing exposure, franchise recognition, and recency, rather than rating alone.

---

# 3️.Franchise Analysis

##  Franchise vs Standalone Comparison

Source: `data/kpis/franchise_vs_standalone.csv`

This comparison evaluates:

* Mean Revenue
* Median ROI
* Mean Budget
* Mean Popularity
* Mean Rating

**Insight:**
Franchise films typically demonstrate consistent financial performance due to brand recognition and audience loyalty. However, standalone films can occasionally generate exceptional outlier success.

---

##  Most Successful Franchises

Source: `data/kpis/most_successful_franchises.csv`

This ranking aggregates:

* Total Movies
* Total Revenue
* Mean Revenue
* Mean Rating

**Insight:**
The dominance of franchise-based intellectual property highlights the increasing concentration of revenue within cinematic universes.

---

# 4️.Director Performance Analysis

##  Most Successful Directors

Source: `data/kpis/most_successful_directors.csv`

This ranking aggregates:

* Total Movies
* Total Revenue
* Mean Rating
* Mean ROI

**Insight:**
Certain directors consistently generate high revenue, indicating strong brand value and audience trust in their productions.

---

#  Overall Strategic Conclusion

The KPI analysis demonstrates:

* A strong positive relationship between production budget and revenue.
* Genre-level variability in ROI, with Fantasy and Romance showing strong efficiency.
* Popularity does not strictly correlate with audience ratings.
* Revenue concentration is increasingly driven by franchise-based productions.
* Standalone films can generate exceptional success but exhibit higher variance.

These findings reflect modern industry dynamics where franchise economics dominate, yet selective standalone innovation remains strategically valuable.

