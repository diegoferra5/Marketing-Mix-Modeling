# 📊 Marketing Mix Modeling (MMM) Project

A concise, end-to-end Marketing Mix Modeling (MMM) pipeline using Python. The repository includes data preparation, adstock & saturation transformations, regression modelling, diagnostics, and outputs for channel contribution and ROI analysis.

---

## Table of contents

- Project layout
- Environment setup
- Key dependencies
- Methodology overview
- Example outputs
- Contribution & contact

---

## Project layout

Root structure (high level)

```text
MMMDemo/
│
├── notebooks/        # EDA, experiments, visualizations (Jupyter)
├── src/              # Core modules (adstock, saturation, preprocessing, modeling)
├── data/             # Raw and processed datasets (git-ignored)
│
├── environment.yml   # Conda environment
├── README.md
└── .gitignore
```

Folder descriptions:

- notebooks/: exploratory notebooks for feature engineering, diagnostics and modeling runs.  
- src/: reusable Python modules:
  - adstock.py — adstock/carryover transforms  
  - saturation.py — saturation curves (Hill / log/Weibull)  
  - preprocessing.py — cleaning and feature construction  
  - model.py — MMM training, inference, and evaluation utilities  
  - utils.py — plotting and helper functions  
- data/: input datasets and derived tables (not checked into VCS).

---

## Environment setup

Create and activate the environment:

```bash
conda env create -f environment.yml
conda activate mmm_env
```

Note: use the channel and package versions pinned in environment.yml for reproducibility.

---

## Key dependencies

- Python 3.10+
- NumPy
- Pandas
- Scikit-learn
- Statsmodels
- Matplotlib / Seaborn
- JupyterLab

---

## Methodology overview

1. Data preparation
   - Validate and clean raw inputs
   - Aggregate to modeling granularity (e.g., weekly)
   - Build media, promo, trend, seasonality, and holiday features

2. Transformations
   - Adstock (geometric, delayed or custom kernels) for carryover
   - Saturation functions (Hill or log-based) for diminishing returns
   - Lag structures and temporal decomposition

3. Modeling
   - Semi-log or multiplicative regression frameworks
   - Parameter estimation with constraints and regularization
   - Diagnostics: residuals, multicollinearity, stability, and holdout tests

4. Outputs
   - Channel contribution and attribution
   - ROI and marginal ROI estimates
   - Scenario simulation and budget reallocation insights

---

## Recommended checks & diagnostics

- Validate date ordering and continuity after aggregation.  
- Inspect adstock/saturation transforms visually to ensure expected shapes.  
- Check VIF / correlation to detect multicollinearity before interpreting coefficients.  
- Use holdout/sanity checks to validate incremental estimates.

---

## Example outputs / visualizations


- Adstock curves per channel
- Saturation curves vs observed ROI
- Contribution waterfall charts
- Budget optimization heatmaps and scenario tables

---

## Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out.