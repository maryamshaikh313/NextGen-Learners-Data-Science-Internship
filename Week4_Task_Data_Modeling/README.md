# Predicting Internship Selection Outcomes

**A simple machine learning project that predicts whether an applicant is likely to be selected for the NextGen Learners internship program, and explains the results honestly in plain language.**

## Objective
This is my Week 4 capstone for the NextGen Learners Data Science internship. My goal was to combine what I learned in Weeks 1–3 (cleaning and exploring data) with a first machine learning model, and then explain my findings clearly for someone who is not technical.

## Dataset
- I used the cleaned applicant dataset from my Week 1 task (`applicants_cleaned_by_maryamshaikh.csv`). It has the applicant name, email, phone, domain applied, university, application date and status.
- It contains **85 applicants**. I removed the 29 applicants who were still "Under Review", because they have no final result to learn from. That left **56 applicants** (36 Selected and 20 Rejected) for the model.
- **Important:** I did not have real data about skills, portfolios or hackathons, so I **simulated four extra features with code**: `num_skills_listed`, `has_portfolio`, `prior_hackathon_participation` and `statement_quality_score`. They are not real applicant data. I used `np.random.seed(42)` so the results can be reproduced, and I saved the extended data in `applicants_with_simulated_features.csv`. Because I built a link between these features and selection into the simulation, my results show how the method works. They are not a real finding about how NextGen Learners selects interns.

## Method
1. Loaded the cleaned Week 1 data.
2. Added the four simulated features.
3. Prepared the data for the model: changed Yes/No to 1/0, created a target column (Selected = 1, otherwise 0), removed "Under Review" rows, and one-hot encoded the Domain column.
4. Split the data into 80% training (44 rows) and 20% testing (12 rows).
5. Trained a Logistic Regression model.
6. Evaluated it using accuracy, precision, recall and a confusion matrix. I also compared it with a baseline and tested 20 different splits to see how stable the results are.
7. Looked at the model's coefficients to see which features mattered most.
8. Wrote an Executive Summary for a non-technical reader.

## Key results
- **Accuracy: 66.7%.** The model predicted the correct result for about two out of three test applicants. However, always guessing "Selected" would also give 66.7%, so accuracy alone does not prove the model is better than guessing.
- **Precision: 83.3%.** When the model predicted "Selected", it was right about 83% of the time.
- **Recall: 62.5%.** The model found about 62% of the applicants who were actually selected.
- **Most important factors:** having a portfolio/GitHub link (by far the strongest), then prior hackathon participation. The statement score had a smaller effect, and the number of listed skills had almost none.
- **Stability:** with different train/test splits, accuracy ranged from 50% to 92%, because the test set is very small.

## Limitations
- The dataset is small and partly simulated.
- The results change a lot depending on the split, so they should be seen as an example of the method, not a guarantee.
- A model can repeat unfair patterns from past decisions, so bias is a real risk.
- The model should only support human reviewers. It should never replace them.

## How to run the notebook
1. Open `Week4_Capstone_MaryamShaikh.ipynb` in Google Colab.
2. Upload `applicants_cleaned_by_maryamshaikh.csv` using the file button on the left side.
3. Click **Runtime → Run all** and wait for all cells to finish.

It needs `pandas`, `numpy`, `matplotlib` and `scikit-learn`, which are already installed in Colab.

## Files in this repository
- `Week4_Capstone_MaryamShaikh.ipynb`: the full notebook with explanations
- `applicants_cleaned_by_maryamshaikh.csv`: cleaned data from Week 1
- `applicants_with_simulated_features.csv`: data with the four simulated features
- `make_simulated_features.py`: small script that recreates the simulated-features file
- `README.md`: this file

## Walkthrough video
Video link:

---
**Author:** Maryam Shaikh | NextGen Learners Data Science Internship
