## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
print(all_ages.loc[:5, :], recent_grads.loc[:5, :])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

#aa_cat_counts = {}
#g_cat_counts = {}

def calculate_totals(df):
    categories = df['Major_category'].unique()
    counts_dict = {}
    for c in categories:
        major_df = df[df['Major_category'] == c]
        total = major_df['Total'].sum()
        counts_dict[c] = total
    return counts_dict

aa_cat_counts = calculate_totals(all_ages)
rg_cat_counts = calculate_totals(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

low_wage_jobs = recent_grads['Low_wage_jobs'].sum()
total_num = recent_grads['Total'].sum()
low_wage_proportion = low_wage_jobs / total_num
print(low_wage_proportion)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    all_ages_row = all_ages[all_ages['Major'] == major]
    recent_grads_row = recent_grads[recent_grads['Major'] == major]
    if recent_grads_row.iloc[0]['Unemployment_rate'] < all_ages_row.iloc[0]['Unemployment_rate']:
        rg_lower_count += 1
print(rg_lower_count)