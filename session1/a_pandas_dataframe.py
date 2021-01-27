# encoding: utf-8

##################################################
# This script shows uses the pandas library to create a dataframe data type
# Later, the data is used to handle descriptive statistics
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2021, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library
import pandas as pd

a_df = pd.read_csv('../data/WB_GDP_growth_anual.csv', skiprows=4)

print('####################')
print('This is how a data frame looks like:')
print(a_df.head())

# Using the following list, we will create a subset to explore summary statistics
countries = ('Spain', 'France', 'Colombia', 'United Kingdom')

# To understand the logics, we will do the task with a single country
name = [countries[0]]
country = pd.DataFrame(name, columns=['name'])
country_values = a_df[a_df['Country Name'] == country['name'][0]]
gdp_growth_values = country_values.iloc[0, 4:]
country['gdp_growth_mean'] = gdp_growth_values.mean()
country['gdp_growth_median'] = gdp_growth_values.median()
country['gdp_growth_max'] = gdp_growth_values.max()
country['gdp_growth_min'] = gdp_growth_values.min()
country['gdp_growth_std'] = gdp_growth_values.std()
print('Summary statistics of GDP for %s' % name)
print(country)

# We can also generalise the procedure through a loop loop
# This empty object will host the summary
columns = ['name', 'gdp_growth_mean', 'gdp_growth_median', 'gdp_growth_max',
           'gdp_growth_min', 'gdp_growth_std']
countries_summary = pd.DataFrame(columns=columns)

for c in countries:
    name = [c]
    country = pd.DataFrame(name, columns=['name'])
    country_values = a_df[a_df['Country Name'] == country['name'][0]]
    gdp_growth_values = country_values.iloc[0, 4:]
    country['gdp_growth_mean'] = gdp_growth_values.mean()
    country['gdp_growth_median'] = gdp_growth_values.median()
    country['gdp_growth_max'] = gdp_growth_values.max()
    country['gdp_growth_min'] = gdp_growth_values.min()
    country['gdp_growth_std'] = gdp_growth_values.std()
    countries_summary = countries_summary.append(country)
countries_summary = pd.DataFrame(countries_summary)
print(countries_summary)

