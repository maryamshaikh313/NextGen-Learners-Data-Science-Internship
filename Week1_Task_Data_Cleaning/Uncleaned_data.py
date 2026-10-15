import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker and set random seed for reproducibility
fake = Faker()
random.seed(42)

print("Status: Initializing raw dataset generation...")

# Define structural variations for generating synthetic messy data
domains = ['Web Development', 'web dev', 'WEB DEV', 'Data Science', 'data science', 'AI','artificial intelligence', 'Graphic Design', 'graphic design', 'Cyber Security', 'cyber security', 'CyberSecurity']
statuses = ['Selected', 'Rejected', 'Under Review', 'selected', None]

data = []

# Generate 85 base records with planned data quality anomalies
for i in range(85):
    # Introduce leading/trailing whitespace anomalies
    name = f"  {fake.name()}  " if i % 5 == 0 else fake.name()
    
    # Introduce inconsistent casing and structural missingness (NaN)
    email = fake.email().upper() if i % 6 == 0 else fake.email()
    email = np.nan if i % 12 == 0 else email
    
    # Introduce inconsistent string delimiter formatting for phone records
    phone = f"0301-{random.randint(1111111, 9999999)}" if i % 2 == 0 else f"0301 {random.randint(1111111, 9999999)}"
    
    # Assign randomized values including structural None types
    domain = random.choice(domains)
    univ = np.nan if i % 9 == 0 else "NED University"
    date = "12/05/2026" if i % 3 == 0 else "2026-05-12"
    status = random.choice(statuses)
    
    data.append([name, email, phone, domain, univ, date, status])

# Construct DataFrame with target schema
df = pd.DataFrame(data, columns=['Applicant Name', 'Email', 'Phone', 'Domain Applied', 'University', 'Application Date', 'Status'])

# Append explicit duplicate records to simulate redundant form submissions
duplicates = df.iloc[0:3]
df = pd.concat([df, duplicates], ignore_index=True)

# Export structural raw dataset to local repository
output_filename = 'applicants_by_maryamshaikh.csv'
df.to_csv(output_filename, index=False)

print("\n" + "="*50)
print("EXECUTION SUCCESSFUL")
print("="*50)
print(f"Output File: {output_filename}")
print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("="*50)
