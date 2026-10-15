import pandas as pd

# Load the generated raw dataset
# Note: Filename has been adjusted to match your exact file
filename = 'applicants_by_maryamshaikh.csv'
df = pd.read_csv(filename)

print("="*60)
print("          PRODUCTION DATA EXPLORATION REPORT")
print("="*60)

# 1. Shape Assessment
print(f"[METRIC] Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n")
print("--------[METRIC] First 5 Rows---------")
print(df.head())

# 2. Schema and Data Type Inspection
print("--- [METRIC] Structural Information ---")
df.info()

# 3. Missing Value Quantification
print("\n--- [METRIC] Missing Values Per Feature Column ---")
print(df.isnull().sum())

# 4. Duplicate Record Quantification
print(f"\n[METRIC] Exact Redundant Rows Count: {df.duplicated().sum()}")
print("="*60)
