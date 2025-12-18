import numpy as np
import pandas as pd

def create_fourier_features(df, trend_col='trend', n_pairs=2, period=52.14):
    """
    Create Fourier features for seasonal modeling.

    Fourier terms capture cyclical patterns (like annual seasonality) using
    sine and cosine functions. They provide a smoother representation than
    discrete month dummies and reduce multicollinearity with trend variables.

    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    trend_col : str
        Column representing sequential time (1, 2, 3, ...)
        Default: 'trend'
    n_pairs : int
        Number of sin/cos pairs to create (1-3 recommended for weekly data)
        - n_pairs=1: Captures primary annual cycle
        - n_pairs=2: Captures primary + first harmonic (recommended)
        - n_pairs=3: Adds more flexibility but increases risk of overfitting
        Default: 2
    period : float
        Seasonality period in same units as trend_col
        For weekly data: 52.14 weeks/year (accounting for leap years)
        For daily data: 365.25 days/year
        Default: 52.14

    Returns:
    --------
    pd.DataFrame
        Copy of original dataframe with added columns:
        - fourier_sin_1, fourier_cos_1 (first pair)
        - fourier_sin_2, fourier_cos_2 (second pair, if n_pairs >= 2)
        - etc.

    Examples:
    ---------
    >>> df = pd.DataFrame({'trend': range(1, 136), 'sales': np.random.randn(135)})
    >>> df_fourier = create_fourier_features(df, n_pairs=2)
    >>> df_fourier.columns
    Index(['trend', 'sales', 'fourier_sin_1', 'fourier_cos_1',
           'fourier_sin_2', 'fourier_cos_2'], dtype='object')

    Notes:
    ------
    - Fourier terms are orthogonal (uncorrelated with each other)
    - They maintain temporal continuity across year boundaries
    - Widely used in MMM frameworks (Google Meridian, Meta Robyn)
    """
    df = df.copy()
    freq = 2 * np.pi / period

    for k in range(1, n_pairs + 1):
        df[f'fourier_sin_{k}'] = np.sin(k * freq * df[trend_col])
        df[f'fourier_cos_{k}'] = np.cos(k * freq * df[trend_col])

    return df
