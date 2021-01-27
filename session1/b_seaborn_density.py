# encoding: utf-8

##################################################
# This script shows uses the pandas library to create a density plots based on
# a dataframe and the seaborn
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
import matplotlib.pyplot as plt
import seaborn as sns

gdp_growth = pd.read_csv('../data/WB_GDP_growth_anual.csv', skiprows=4)

# Using the following list, we will create a subset to explore summary statistics
countries = ('Spain', 'France', 'Colombia', 'United Kingdom')

# First, we will create an histogram for the values in 2019

# matplotlib histogram
plt.hist(gdp_growth['2019'], color='blue', edgecolor='black', bins=20)

# seaborn histogram
sns.distplot(gdp_growth['2019'], hist=True, kde=False, bins=20, color='blue',
             hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Histogram of GDP growth in 2019')
plt.xlabel('Growth (%)')
plt.ylabel('Frequency')



# Second, we can create a histogram for a single country
# To understand the logics, we will do the task with a single country
name = [countries[0]]
country = pd.DataFrame(name, columns=['name'])
country_values = gdp_growth[gdp_growth['Country Name'] == country['name'][0]]
gdp_growth_values = country_values.iloc[0, 4:]

# matplotlib histogram
plt.hist(gdp_growth_values, color='blue', edgecolor='black', bins=20)

# seaborn histogram
sns.distplot(gdp_growth_values, hist=True, kde=False, bins=20, color='blue',
             hist_kws={'edgecolor':'black'})
# Add labels
plt.title('GDP growth in %s' % name)
plt.xlabel('Growth (%)')
plt.ylabel('frequency')



# Third, For density plots refer to the following documentation
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0#:~:text=Density%20Plots%20in%20Seaborn&text=The%20curve%20shows%20the%20density,scale%20as%20the%20density%20plot.
# Density Plot and Histogram of all arrival delays
sns.distplot(gdp_growth_values, hist=True, kde=True,
             bins=40, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})


print('Compare multiple countries and analyse')