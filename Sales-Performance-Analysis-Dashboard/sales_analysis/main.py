# main.py

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../superstore.csv")  # go up one level to access CSV

# Quick look
print("Dataset shape:", df.shape)
print(df.head())

# Basic info
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Sales by category
plt.figure(figsize=(8, 5))
sns.barplot(x="Category", y="Sales", data=df, estimator=sum, ci=None)
plt.title("Total Sales by Category")
plt.show()

# Profit by region
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Profit", data=df, estimator=sum, ci=None)
plt.title("Total Profit by Region")
plt.show()

# Sales vs Profit scatterplot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Sales", y="Profit", hue="Category", data=df)
plt.title("Sales vs Profit")
plt.show()
