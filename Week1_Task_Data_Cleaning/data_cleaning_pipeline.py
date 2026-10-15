import pandas as pd

source_file = 'applicants_by_maryamshaikh.csv'
df = pd.read_csv(source_file)

print("=" * 60)
print("          DATA CLEANING PIPELINE")
print("=" * 60)
print(f"[INFO] Initial dimensions before cleaning: {df.shape}\n")

# STEP 4: MISSING VALUES
df = df.dropna(subset=['Applicant Name'])
df['University'] = df['University'].fillna('Not Specified')
df['Status'] = df['Status'].fillna('Under Review')
print("[SUCCESS] Step 4: Missing values handled.")

# STEP 5: DUPLICATES
df = df.drop_duplicates()
df['Email'] = df['Email'].str.strip().str.lower()
df = df[df['Email'].isna() | ~df.duplicated(subset='Email')]
df['Email'] = df['Email'].fillna('not_provided@example.com')
print("[SUCCESS] Step 5: Duplicates removed.")

# STEP 6: STANDARDIZE TEXT
df['Applicant Name'] = df['Applicant Name'].str.strip().str.title()

domain_mapping = {
    'web development': 'Web Development',
    'web dev': 'Web Development',
    'webdev': 'Web Development',
    'data science': 'Data Science',
    'ai': 'Artificial Intelligence',
    'artificial intelligence': 'Artificial Intelligence',
    'cyber security': 'Cyber Security',
    'cybersecurity': 'Cyber Security',
    'graphic design': 'Graphic Design',
}
clean_domain = df['Domain Applied'].str.strip().str.lower()
mapped = clean_domain.map(domain_mapping)
print("Unmapped domain values:", clean_domain[mapped.isna() & clean_domain.notna()].unique())
df['Domain Applied'] = mapped.fillna('Not Specified')

df['Status'] = df['Status'].str.strip().str.title()
print("[SUCCESS] Step 6: Text standardized.")

# STEP 7: DATA TYPES
iso_dates = pd.to_datetime(df['Application Date'], format='%Y-%m-%d', errors='coerce')
slash_dates = pd.to_datetime(df['Application Date'], format='%d/%m/%Y', errors='coerce')
df['Application Date'] = iso_dates.fillna(slash_dates)
df['Phone'] = df['Phone'].str.replace('-', '', regex=False).str.replace(' ', '', regex=False)
print("[SUCCESS] Step 7: Data types fixed.")

# STEP 9: EXPORT
output_file = 'applicants_cleaned_by_maryamshaikh.csv'
df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print(f"Final dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
print("Domain values:", df['Domain Applied'].unique())
print("Missing values:\n", df.isnull().sum())
print("=" * 60)
