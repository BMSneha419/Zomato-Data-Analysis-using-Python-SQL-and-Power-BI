# Importing the required Libraries

import pandas as pd
import numpy as np

# Loading the Dataset
# Loading the CSV file into a pandas DataFrame
df = pd.read_csv("zomato_dataset_cleaned.csv")

# PRICE CATEGORY

def price_bucket(price):
    if price <= 100:
        return "Low"
    elif price <= 300:
        return "Medium"
    else:
        return "High"

df["Price_Category"] = df["Average Price"].apply(price_bucket)

# RATING CATEGORY

def rating_bucket(rating):
    if pd.isna(rating):
        return "Unrated"
    elif rating < 3.5:
        return "Low Rated"
    elif rating < 4.2:
        return "Moderate Rated"
    else:
        return "Highly Rated"

df["Rating_Category"] = df["Rating"].apply(rating_bucket)

# DELIVERY SPEED CATEGORY

def delivery_bucket(time):
    if time <= 20:
        return "Fast"
    elif time <= 40:
        return "Moderate"
    else:
        return "Slow"

df["Delivery_Speed_Category"] = df["Average Delivery Time"].apply(delivery_bucket)

# VALUE FOR MONEY SCORE

df["Value_for_Money_Score"] = df["Rating"] / df["Average Price"]

# CUISINE FEATURES

df["Cuisine_Count"] = df["Cuisine"].apply(lambda x: len(x.split(",")))
df["Is_Multi_Cuisine"] = df["Cuisine_Count"].apply(lambda x: True if x > 1 else False)

# LOCATION-BASED FEATURES

df["Location_Avg_Rating"] = df.groupby("Location")["Rating"].transform("mean")
df["Location_Avg_Price"] = df.groupby("Location")["Average Price"].transform("mean")
df["Location_Avg_Delivery"] = df.groupby("Location")["Average Delivery Time"].transform("mean")

# SAFETY FLAG

df["Safety_Flag"] = df["Safety Measure"].apply(
    lambda x: 1 if x.lower() != "not available" else 0
)


# Final Dataset Info

print("\nFinal Dataset Info After Feature Engineering:")
print(df.info())

print("\nSample Rows:")
print(df.head())

# Saving the feature-engineered dataset

df.to_csv("zomato_dataset_feature_engineered.csv", index=False)

print("\nFeature Engineering completed successfully.")
