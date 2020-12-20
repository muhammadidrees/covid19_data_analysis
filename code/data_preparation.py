# Before performing any analysis we need to check the data
# and prepare it excluding null values and giving proper
# format to values so our data can be clean and ready

import pandas as pd
import numpy as np
import pycountry

# covert the data file into a dataframe so it's easy to manupilate
covid = pd.read_csv("data/covid_19_data.csv")

# show the head so we know exactly what data are we dealing with
print("\nInitial 5 rows of data:\n", covid.head())

# to get a better understanding of the numerical data
print("\nReport of numerical data:\n", covid.describe())

# show the size and shape of data
print("\nSize and shape of data:", covid.shape)

# check null values in each column
print("\nNull values in columns:\n", covid.isnull().sum())

# droping S No, province/state and Last Update columns 
covid.drop(["SNo", "Province/State", "Last Update"], 1, inplace=True)

# verifying update
print("\nAfter droping columns:\n")
print(covid.head())

# converting "Observation Date" to date time format
covid["ObservationDate"] = pd.to_datetime(covid["ObservationDate"])

# verifying update
print("\nAfter formatting observation date:\n")
print(covid.head())

grouped_country=covid.groupby(["Country/Region"], as_index=False).agg({"Confirmed":'sum',"Recovered":'sum',"Deaths":'sum'})

print("\nAfter formatting observation date:\n")
print(grouped_country.head())
print(grouped_country.shape)

list_of_countries = [country.name for country in list(pycountry.countries)]
wrong_names = []
r = 0
def get_wrong_countries(row):
    global r
    for country in list_of_countries:
        if country in row["Country/Region"]:
            r = r + 1
            return country
    wrong_names.append(row["Country/Region"])    
    return 
    # return row['height'] * row['width']

print(grouped_country.apply(get_wrong_countries, axis=1))
print(wrong_names)

print()
print(r)
print()
print()
print(list_of_countries)

# print("\nNull values in columns:\n", grouped_country.)
# print(covid["Country/Region"].str.len())
# print(covid.groupby("Country/Region", as_index=False).apply(lambda x: x[x["Country/Region"].str.len() == x["Country/Region"].str.len().max()]))

# country_len = covid["Country/Region"].str.len()

# print(covid.pivot_table(index = ["Country/Region"], aggfunc ='size'))
# dups = df.pivot_table(index = ['Course'], aggfunc ='size')
# print(len(pycountry.countries)) 