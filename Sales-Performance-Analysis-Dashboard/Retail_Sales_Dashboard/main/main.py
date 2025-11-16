import os
import pandas as pd

# Get current script folder
base_dir = os.path.dirname(os.path.abspath(__file__))

# Find CSV (handles .csv.csv too)
csv_files = [f for f in os.listdir(base_dir) if f.lower().endswith(".csv")]

if not csv_files:
    print(f"❌ No CSV file found in {base_dir}")
else:
    csv_path = os.path.join(base_dir, csv_files[0])

    # Auto-rename if .csv.csv
    if csv_path.lower().endswith(".csv.csv"):
        new_path = csv_path[:-4]  # remove extra ".csv"
        os.rename(csv_path, new_path)
        csv_path = new_path
        print(f"🔄 Renamed to: {csv_path}")

    print(f"📂 Using CSV: {csv_path}")

    try:
        df = pd.read_csv(csv_path, encoding="latin1")
        print("✅ CSV loaded successfully")
        print(df.head())
    except Exception as e:
        print(f"❌ Still failed. Error: {e}")


