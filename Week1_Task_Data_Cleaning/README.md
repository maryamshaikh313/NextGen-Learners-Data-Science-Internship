# NextGen Learners - Data Science Internship

## Task 1: Cleaning & Exploring the Applicant Dataset (Week 1)

**Intern:** Maryam Shaikh

This task cleans a raw applicant dataset using Pandas. Every fix is done in code, so the whole process can be re-run from the raw file.

---

## Files in this repository

| File | Purpose |
|---|---|
| `Uncleaned_data.py` | Generates the messy raw dataset |
| `applicants_by_maryamshaikh.csv` | Raw (uncleaned) dataset |
| `data_exploration.py` | First look at the raw data (before cleaning) |
| `data_cleaning_pipeline.py` | Full cleaning pipeline |
| `applicants_cleaned_by_maryamshaikh.csv` | Final cleaned dataset |
| `Cleaned_data_verification.py` | Checks the cleaned data (after cleaning) |
| `Week1_Data_Cleaning_MaryamShaikh.ipynb` | Notebook with code and written explanations |

---

## Data Quality Summary

### 1. Before Cleaning

- **Size:** 88 rows, 7 columns
- **Missing values:** 34 in total (Email: 9, University: 11, Status: 14)
- **Duplicates:** 3 exact duplicate rows
- **Text problems:** extra spaces in names, inconsistent email casing, and many spellings of the same domain (e.g. `web dev`, `WEB DEV`, `Web Development`)
- **Wrong data types:** Application Date stored as text, not as a date
- **Phone numbers:** mixed formats with dashes and spaces

### 2. What Was Done

- **Missing values:**
  - Rows with a missing Applicant Name are dropped, because a nameless application cannot be used (none were found in this dataset).
  - Missing University is filled with `Not Specified`, since it is not essential for an application.
  - Missing Status is filled with `Under Review`, since a blank usually means the application is not processed yet.
  - Missing Email is filled with `not_provided@example.com` so the applicant is kept. This is done after duplicate removal.
- **Duplicates:**
  - Exact duplicate rows are removed first (3 found).
  - Emails are lowercased and checked for duplicates, ignoring missing emails. No duplicate emails were found, so no applicants were lost.
- **Text standardization:**
  - Names are trimmed and converted to Title Case.
  - A mapping dictionary converts all domain spellings into 5 standard tracks.
  - Status is trimmed and converted to Title Case.
- **Data types:**
  - Application Date is converted to a real datetime (`datetime64`). The data has two formats (`2026-05-12` and `12/05/2026`), so each format is parsed explicitly and combined. Unreadable dates become `NaT` (`errors='coerce'`).
  - Phone numbers are cleaned of dashes and spaces and kept as text.

### 3. After Cleaning

- **Size:** 85 rows, 7 columns
- **Missing values:** 0
- **Exact duplicates:** 0
- **Duplicate real emails:** 0 (the placeholder email marks "email not given" and is not counted as a duplicate)
- **Application Date:** confirmed as `datetime64`
- **Domain Applied:** exactly 5 clean tracks: Web Development, Data Science, Artificial Intelligence, Graphic Design, Cyber Security

---

## How to run

1. `python Uncleaned_data.py` creates the raw dataset.
2. `python data_exploration.py` shows the before-cleaning checks.
3. `python data_cleaning_pipeline.py` cleans the data and saves the cleaned CSV.
4. `python Cleaned_data_verification.py` confirms the cleaned data.

The same steps with full written explanations are in the notebook.