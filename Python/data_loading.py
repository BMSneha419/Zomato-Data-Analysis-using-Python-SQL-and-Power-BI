# Importing the required Libraries

import pandas as pd
import numpy as np

# Loading the Dataset
# Loading the CSV file into a pandas DataFrame
df = pd.read_csv("zomato_dataset.csv")

# Initial Data Preview
# Displaying the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Dataset Dimensions

print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# Column Names

print("\nColumn Names:")
print(df.columns)

# Data Types of Columns

print("\nData Types:")
print(df.dtypes)

# Summary Statistics (Numerical Columns)

print("\nSummary Statistics:")
print(df.describe())

# Categorical Columns Overview

print("\nTop 10 Cuisines:")
print(df["Cuisine"].value_counts().head(10))

print("\nTop 10 Locations:")
print(df["Location"].value_counts().head(10))

print("\nSafety Measure Distribution:")
print(df["Safety Measure"].value_counts())

# Missing Values Check

print("\nMissing Values Count:")
print(df.isna().sum())


print("\nData loading and initial understanding completed.")
