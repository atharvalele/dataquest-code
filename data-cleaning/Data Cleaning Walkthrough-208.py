## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for file in data_files:
    df = pd.read_csv('schools/' + file)
    key = file.replace('.csv', '')
    data[key] = df

## 5. Exploring the SAT Data ##

print(data['sat_results'].head())

## 6. Exploring the Remaining Data ##

for df in data:
    print(data[df].head())

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)
print(survey.head())

## 9. Cleaning Up the Surveys ##

survey['DBN'] = survey['dbn']
required_coulmns = ['DBN', 'rr_s', 'rr_t', 'rr_p', 'N_s', 'N_t', 'N_p', 'saf_p_11', 'com_p_11', 'eng_p_11', 'aca_p_11', 'saf_t_11', 'com_t_11', 'eng_t_11', 'aca_t_11', 'saf_s_11', 'com_s_11', 'eng_s_11', 'aca_s_11', 'saf_tot_11', 'com_tot_11', 'eng_tot_11', 'aca_tot_11']
survey = survey[required_coulmns]
data['survey'] = survey

## 11. Inserting DBN Fields ##

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

def pad(num):
    string = str(num)
    if len(string) > 1:
        return string
    else:
        return string.zfill(2)
    
data['class_size']['padded_csd'] = data['class_size']['CSD'].apply(pad)
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']
print(data['class_size'].head())

## 12. Combining the SAT Scores ##

scores = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']

for score in scores:
    data['sat_results'][score] = pd.to_numeric(data['sat_results'][score], errors='coerce')

data['sat_results']['sat_score'] = data['sat_results'][scores[0]] + data['sat_results'][scores[1]] + data['sat_results'][scores[2]]

print(data['sat_results']['sat_score'].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re

def get_lat(string):
    coordinates = re.findall('\(.+\)', string)
    lat = coordinates[0].split(',')[0].replace('(', '')
    return lat

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(get_lat)
print(data['hs_directory'].head())

## 14. Extracting the Longitude ##

import re

def get_long(string):
    coordinates = re.findall('\(.+\)', string)
    long = coordinates[0].split(',')[1].replace(')', '').strip()
    return long

data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(get_long)

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')
print(data['hs_directory'].head())