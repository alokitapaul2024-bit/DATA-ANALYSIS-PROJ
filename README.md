# Task 1: Data Cleaning and Preprocessing

>Dataset
Google Ads Sales Dataset (Uncleaned)   [from: kaggle.com]

## Tools Used

Python, Pandas

## What I Did
1. Renamed column headers to lowercase with underscores
2. Handled missing values by filling with mode or 'unknown'
3. Checked for duplicates (not found)
4. Standardized device column casing (Desktop/Mobile/Tablet)
5. Fixed location typos (hyderbad, hydrebad → Hyderabad)
6. Fixed campaign name spelling mistakes
7. Converted ad_date to datetime handling 3 mixed formats to a single type of format as 'dd-mm-yyyy'
8. Converted clicks, impressions, leads, conversions to integer
9. Rounded conversion_rate to 3 decimal places
10. Saving the data to csv file

## Result
- Original: 2600 rows × 13 columns
- Cleaned: 2600 rows × 13 columns
- Cleaned dataset saved as cleaned_data.csv
