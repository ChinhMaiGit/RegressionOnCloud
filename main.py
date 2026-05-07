import pandas as pd
import numpy as np
import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ── Load Data ──────────────────────────────────────────
housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['Price'] = housing.target

print("First 5 rows:")
print(df.head())
print("\nData Summary:")
print(df.describe())