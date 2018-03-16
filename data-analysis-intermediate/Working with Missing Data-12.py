## 2. Introduction ##

import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

## 3. Finding the Missing Data ##

age = titanic_survival["age"]
print(age.loc[10:20])
age_null = pd.isnull(age)
age_null_true = age[age_null]
age_null_count = len(age_null_true)

## 4. Whats the big deal with missing data? ##

age_is_null = pd.isnull(titanic_survival["age"])
age_not_null = age[age_is_null == False]
correct_mean_age = sum(age_not_null) / len(age_not_null)

## 5. Easier Ways to Do Math ##

correct_mean_age = titanic_survival['age'].mean()
correct_mean_fare = titanic_survival['fare'].mean()

## 6. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}
for cl in passenger_classes:
    pclass = titanic_survival[titanic_survival['pclass'] == cl]
    pclass_fare = pclass['fare']
    fares_by_class[cl] = pclass_fare.mean()

## 7. Making Pivot Tables ##

import numpy as np
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index='pclass', values='age', aggfunc=np.mean)

## 8. More Complex Pivot Tables ##

import numpy as np
port_stats = titanic_survival.pivot_table(index = 'embarked', values = ['survived', 'fare'], aggfunc = np.sum)
print(port_stats)

## 9. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis = 1)
new_titanic_survival = titanic_survival.dropna(axis = 0, subset = ['age', 'sex'])

## 10. Using iloc to Access Rows by Position ##

# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]

## 11. Using Column Indexes ##

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,'age']
row_index_766_pclass = new_titanic_survival.loc[766,'pclass']
row_index_1100_age = new_titanic_survival.loc[1100, 'age']
row_index_25_survived = new_titanic_survival.loc[25, 'survived']
five_rows_three_cols = new_titanic_survival.iloc[:5, :3]                  

## 12. Reindexing Rows ##

titanic_reindexed = new_titanic_survival.reset_index(drop = True)
print(titanic_reindexed.iloc[:5, :3])

## 13. Apply Functions Over a DataFrame ##

def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row_var = titanic_survival.apply(hundredth_row)

def count_null(series):
    null_items = series.isnull()
    return len(series[null_items])

column_null_count = titanic_survival.apply(count_null)

## 14. Applying a Function to a Row ##

def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)

def get_minors(row):
    if row['age'] < 18:
        return 'minor'
    elif row['age'] >= 18:
        return 'adult'
    else:
        return 'unknown'
    
age_labels = titanic_survival.apply(get_minors, axis = 1)

## 15. Calculating Survival Percentage by Age Group ##

age_group_survival = titanic_survival.pivot_table(index = 'age_labels', values = 'survived')