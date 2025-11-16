import pandas as pd
import os

# Get current folder (main)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
INPUT_FILE = os.path.join(BASE_DIR, "superstore.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "superstore_clean.csv")

print("Reading from:", INPUT_FILE)

try:
    # Load dataset
    df = pd.read_csv(INPUT_FILE, encoding="latin1")
    print("✅ Data loaded successfully")
    print("Shape before cleaning:", df.shape)

    # Drop duplicates
    df = df.drop_duplicates()
    print("Shape after removing duplicates:", df.shape)

    # Drop rows with missing values
    print("Missing values before:\n", df.isnull().sum())
    df = df.dropna()
    print("Shape after removing missing rows:", df.shape)

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # Ensure numeric columns
    num_cols = ["Sales", "Quantity", "Discount", "Profit"]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with invalid data
    df = df.dropna(subset=["Order Date", "Ship Date"] + num_cols)

    # Save cleaned dataset
    df.to_csv(OUTPUT_FILE, index=False)
    print("✅ Cleaned CSV saved to:", OUTPUT_FILE)

    # Preview cleaned data
    print(df.head())

except Exception as e:
    print("❌ Error:", e)
