# Importing the required Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the Dataset
# Loading the CSV file into a pandas DataFrame
df = pd.read_csv("zomato_dataset_cleaned.csv")

# Basic info check
print(df.info())

# Descriptive Statistics

print(df.describe())

# DISTRIBUTION OF RATINGS

plt.figure()
sns.histplot(df["Rating"].dropna(), bins=20)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# BOX PLOT OF RATINGS

plt.figure()
sns.boxplot(x=df["Rating"])
plt.title("Boxplot of Ratings")
plt.show()

# DISTRIBUTION OF AVERAGE PRICE

plt.figure()
sns.histplot(df["Average Price"], bins=30)
plt.title("Distribution of Average Price")
plt.xlabel("Price (₹)")
plt.ylabel("Count")
plt.show()

# BOX PLOT OF AVERAGE PRICE

plt.figure()
sns.boxplot(x=df["Average Price"])
plt.title("Boxplot of Average Price")
plt.show()

# DISTRIBUTION OF DELIVERY TIME

plt.figure()
sns.histplot(df["Average Delivery Time"], bins=30)
plt.title("Distribution of Delivery Time")
plt.xlabel("Minutes")
plt.ylabel("Count")
plt.show()

# BOX PLOT OF DELIVERY TIME

plt.figure()
sns.boxplot(x=df["Average Delivery Time"])
plt.title("Boxplot of Delivery Time")
plt.show()

# TOP 10 LOCATIONS OR CITIES BY RESTAURANT COUNT

top_locations = df["Location"].value_counts().head(10)

plt.figure()
top_locations.plot(kind="bar")
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Restaurant Count")
plt.show()

# TOP 10 CUISINES

top_cuisines = df["Cuisine"].value_counts().head(10)

plt.figure()
top_cuisines.plot(kind="bar")
plt.title("Top 10 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Count")
plt.show()

# TOP 10 LOCATIONS OR CITIES BY RATING

avg_rating_city = df.groupby("Location")["Rating"].mean().sort_values(ascending=False).head(10)

plt.figure()
avg_rating_city.plot(kind="bar")
plt.title("Top 10 Cities by Average Rating")
plt.ylabel("Average Rating")
plt.show()

# PRICE VS RATING

plt.figure()
sns.scatterplot(x="Average Price", y="Rating", data=df)
plt.title("Price vs Rating")
plt.show()


# DELIVERY TIME VS RATING

plt.figure()
sns.scatterplot(x="Average Delivery Time", y="Rating", data=df)
plt.title("Delivery Time vs Rating")
plt.show()


# DELIVERY TIME BY CITY (TOP 10)

avg_delivery_city = df.groupby("Location")["Average Delivery Time"].mean().sort_values().head(10)

plt.figure()
avg_delivery_city.plot(kind="bar")
plt.title("Top 10 Fastest Delivery Cities")
plt.ylabel("Minutes")
plt.show()


# SAFETY MEASURE DISTRIBUTION

plt.figure()
df["Safety Measure"].value_counts().plot(kind="bar")
plt.title("Safety Measure Distribution")
plt.ylabel("Count")
plt.show()

print("Exploratory Data Analysis completed successfully.")
