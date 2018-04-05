## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] >= 1960]

## 5. Consolidating Deaths ##

def calc_deaths(row):
    deaths = 0
    cols = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    for c in cols:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            deaths += 1
    return deaths

true_avengers['Deaths'] = true_avengers.apply(calc_deaths, axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)