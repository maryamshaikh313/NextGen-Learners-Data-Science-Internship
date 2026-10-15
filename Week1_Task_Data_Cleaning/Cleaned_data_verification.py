import pandas as pd

cleaned_file = 'applicants_cleaned_by_maryamshaikh.csv'
df_clean = pd.read_csv(cleaned_file, dtype={'Phone': str}, parse_dates=['Application Date'])

print("=" * 60)
print("          POST-CLEANING VERIFICATION REPORT")
print("=" * 60)

print(f"[METRIC] Dimensions: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns\n")

print(f"[METRIC] Exact Redundant Rows: {df_clean.duplicated().sum()}")
real = df_clean[df_clean['Email'] != 'not_provided@example.com']
print(f"[METRIC] Duplicate Real Emails: {real['Email'].duplicated().sum()}\n")

print("--- [AUDIT] Missing Values ---")
print(df_clean.isnull().sum())

print("\n--- [AUDIT] Data Types ---")
print(df_clean.dtypes)

print("\n--- [AUDIT] Domain Applied (should be exactly 5) ---")
print(df_clean['Domain Applied'].unique())
print("Count:", df_clean['Domain Applied'].nunique())
print("=" * 60)


