# Before performing any analysis we need to check the data
# and prepare it excluding null values and giving proper
# format to values so our data can be clean and ready

import pandas as pd
import numpy as np

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

# check for negative values in numeric columns
print("Negative values in confirmed column: ", len(covid.loc[covid["Confirmed"] < 0]))
print("Negative values in deaths column: ", len(covid.loc[covid["Deaths"] < 0]))
print("Negative values in recovered column: ", len(covid.loc[covid["Recovered"] < 0]))

# droping S. No., province/state and Last Update columns 
covid.drop(["SNo", "Province/State", "Last Update"], 1, inplace=True)

# verifying update
print("\nAfter droping columns:\n")
print(covid.head())

# converting "Observation Date" to date time format
covid["ObservationDate"] = pd.to_datetime(covid["ObservationDate"])

# verifying update
print("\nAfter formatting observation date:\n")
print(covid.head())

# give unique values
unique_countries = covid["Country/Region"].unique()

# print out countries to see the unique one's and check
# for any repeating or wrong data
for a, b, c, d, e in zip(*[iter(unique_countries)]*5):
    print("{:35s} {:35s} {:35s} {:35s} {:35s}\n".format(a, b, c, d, e))

# no. of unique countires
print("Number of unique contry names: ", len(unique_countries))

# printing showed some countries have punctuations and also leading traling spaces
# also Bahamas and Gambia were repeated multiple times so we have to remove this
# ambiguity and renaming china US and UK to give them proper names

# remove punctuation
covid["Country/Region"] = covid["Country/Region"].str.replace(r'[^\w\s]','')

# extra spaces in country names
covid["Country/Region"] = covid["Country/Region"].str.strip()

# convert all instances of Bahamas to Bahamas
covid["Country/Region"] = covid["Country/Region"].apply(lambda x: "Bahamas" if "Bahamas" in x else x)

# convert all instances of Gambia to Gambia
covid["Country/Region"] = covid["Country/Region"].apply(lambda x: "Gambia" if "Gambia" in x else x)

# convert all instances of China to China
covid["Country/Region"] = covid["Country/Region"].apply(lambda x: "China" if "China" in x else x)

# convert all instances of US to United States
covid["Country/Region"] = covid["Country/Region"].apply(lambda x: "US" if "United States" in x else x)

# convert all instances of UK to United Kingdom
covid["Country/Region"] = covid["Country/Region"].apply(lambda x: "UK" if "United Kingdom" in x else x)

# give unique values
unique_countries = covid["Country/Region"].unique()

print()

for a, b, c, d, e in zip(*[iter(unique_countries)]*5):
    print("{:35s} {:35s} {:35s} {:35s} {:35s}\n".format(a, b, c, d, e))

# no. of unique countires after cleaning
print("Number of unique contry names after cleaning: ", len(unique_countries))

covid.to_csv("data/covid_19_clean_data.csv")