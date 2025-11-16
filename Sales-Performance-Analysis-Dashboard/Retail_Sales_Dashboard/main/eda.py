import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLEAN_FILE = os.path.join(BASE_DIR, "superstore_clean.csv")

# Load cleaned dataset
df = pd.read_csv(CLEAN_FILE)
print("✅ Data loaded for EDA, shape:", df.shape)

# --- 1. Sales by Category ---
plt.figure(figsize=(6,4))
sns.barplot(x="Category", y="Sales", data=df, estimator=sum, ci=None)
plt.title("Total Sales by Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "sales_by_category.png"))
plt.show()

# --- 2. Sales by Region ---
plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Sales", data=df, estimator=sum, ci=None)
plt.title("Total Sales by Region")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "sales_by_region.png"))
plt.show()

# --- 3. Profit vs Discount ---
plt.figure(figsize=(6,4))
sns.scatterplot(x="Discount", y="Profit", data=df, alpha=0.5)
plt.title("Profit vs Discount")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "profit_vs_discount.png"))
plt.show()

# --- 4. Monthly Sales Trend ---
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,4))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "monthly_sales_trend.png"))
plt.show()

print("📊 EDA completed. Charts saved in:", BASE_DIR)
