# Importing the required Libraries

import pandas as pd
import numpy as np

# Loading the Dataset
# Loading the CSV file into a pandas DataFrame
df = pd.read_csv("zomato_dataset.csv")

# Create a copy of the DataFrame
clean_df = df.copy()


# Handling Duplicates
# Marking duplicates but not removing them (for transparency)
clean_df["Is_Duplicate"] = clean_df.duplicated(keep="first")

# Cleaning the Rating Column
# Convert rating to numeric
# Converting the Invalid values such as '-', 'New' to NaN
# Ratings are intentionally NOT imputed
clean_df["Rating"] = pd.to_numeric(clean_df["Rating"], errors="coerce")

# Cleaning the Average Price Column
# Invalid values such as 'for one' converted to NaN and handled via imputation.
clean_df["Average Price"] = (
    clean_df["Average Price"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+)")
    .astype(float)
)

# Cleaning the Average Delivery Time Column
# Extracting ONLY delivery durations explicitly stated in minutes
clean_df["Average Delivery Time"] = (
    clean_df["Average Delivery Time"]
    .astype(str)
    .str.extract(r"(\d+)\s*min")
    .astype(float)
)

# Handling missing values in Cuisine Column

clean_df["Cuisine"] = clean_df["Cuisine"].fillna("Unknown")

# Standardizing the Text Columns

text_columns = ["Restaurant Name", "Cuisine", "Safety Measure", "Location"]

for col in text_columns:
    clean_df[col] = clean_df[col].astype(str).str.strip()

# Normalizing cuisine formatting
clean_df["Cuisine"] = clean_df["Cuisine"].str.replace(", ", ",", regex=False)

# Safe Median Function

def safe_median(series):
    
    return series.median() if series.notna().any() else np.nan

# Imputing Average Delivery Time
# Step 1: Location-wise median
clean_df["Average Delivery Time"] = clean_df.groupby("Location")[
    "Average Delivery Time"
].transform(lambda x: x.fillna(safe_median(x)))

# Step 2: Global median fallback
global_delivery_median = clean_df["Average Delivery Time"].median()
clean_df["Average Delivery Time"] = clean_df["Average Delivery Time"].fillna(
    global_delivery_median
)

# Imputing Average Price
# Step 1: Location-wise median
clean_df["Average Price"] = clean_df.groupby("Location")[
    "Average Price"
].transform(lambda x: x.fillna(safe_median(x)))

# Step 2: Global median fallback
global_price_median = clean_df["Average Price"].median()
clean_df["Average Price"] = clean_df["Average Price"].fillna(
    global_price_median
)

# Final Data Validation
print("Final Dataset Info:")
print(clean_df.info())

print("\nMissing Values After Cleaning:")
print(clean_df.isna().sum())

# Saving the cleaned dataset
clean_df.to_csv("zomato_dataset_cleaned.csv", index=False)

print("\nData Cleaning and Preprocessing completed. Cleaned dataset saved.")
