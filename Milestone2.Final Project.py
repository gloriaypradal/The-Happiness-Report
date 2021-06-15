# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:33:02 2020

@author: Gloria
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#reading csv file with raw data
df = pd.read_csv("happiness report-2005-2019.csv")

print(df.head(10))
print(df.shape)

#checking column names and which ones do I need for the study and not, changing names to columns
def check_colnames(df):
    for col in df.columns:
        print(col)

check_colnames(df)

#moving column 'Year' to index 0
Year = df['year']
df.drop(labels=['year'], axis=1,inplace = True)
df.insert(0, 'year', Year)
print(df.head())

check_colnames(df)



#From the previous study, the Happiness score is basiclaly calculated for most of the years in the data set, using 6 variables (see document attach)
#form the previous study the variable with highr statistically signignificant correlation with the happiness score are: Corruption, Life Expectancy, GDP and Health
#In order to analyize this data, I am going to apply subseting to the data frame, keeping just the variables of interest (6 factors),howoever I am going to keep Democratic Quality and Confidence in national government as extension of this anlaysis

df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12]]

print(df.head())
print(df.shape)

#Changing columns names to an easier code

col_names = ['Year', 'Country', 'Happiness_Index', 'GDP', 'Social_Support', 'Life_exp', 'Freedom', 'Generosity', 'Corruption', 'ConfiGover', 'DemocraticQ']


df.columns = col_names

check_colnames(df)

#Group by year

df.groupby(['Year', 'Country'])
print(df.head(20))

#Identifying which years has less data to dropp those rows and work with the last 8 years
year = [x for x in range(2005, 2020)]

plt.figure(figsize=(10,6))
plt.hist(df['Year'], bins = 15)
plt.xticks(year)
plt.show()
#subsetting (rows) years < 2011

df_final = df[df.Year > 2011]
print("Filtered data with correct # of columns and rows has: {} shape".format(df_final.shape))
print(df_final.head(20))

#identify and handle missing values with original data frame

def miss_qu(df, col_names):
    for c in col_names:
        print(c, "has NaN values: %s" %df[c].isnull().values.any())

miss_qu(df, col_names)

#Because of GDP column has NAn values, and this is the focus on the analysis
# I am going to fill the Nan values, with the mean of GDP of the rest of the years in that country

print("Verifyinf existing missing values in modified data set\n")
miss_qu(df_final, col_names)

print("New data fram has Nan values on the GDP column and the rest of the variablles\n")

#Because the data frame is group by year and by country, I'll fill the Nan values with the next value on the column, using .ffill


df_no_miss = df_final.fillna(method='ffill')
print(df_no_miss.head(20))

#checking missing values after filled them

miss_qu(df_no_miss, col_names)
print("NO missing values in the data set\n")

#checking for outliers on GDP variables and Happiness Index

plt.boxplot(df_no_miss['GDP'])
plt.show()
plt.hist(df_no_miss['GDP'], bins = 25)
plt.show()

plt.boxplot(df_no_miss['Happiness_Index'])
plt.show()
plt.hist(df_no_miss['Happiness_Index'], bins = 25)
plt.show()



cont = pd.read_csv("countryContinent.csv")


