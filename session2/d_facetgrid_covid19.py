# encoding: utf-8

##################################################
# This script shows how to collect data from remote sources and create bar plots
# Find extra documentation for the source code here:
# https://github.com/diegopajarito/COVID19_datavis
# Note: the project does not have changes after mid 2019
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
import numpy as np

# Setting up data sources (files and web)
gdp_growth = pd.read_csv('../data/WB_GDP_growth_anual.csv', skiprows=4)
jhu_link_confirmed = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
jhu_link_deaths = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
confirmed = pd.read_csv(jhu_link_confirmed)
confirmed = confirmed.iloc[:, 1:]
confirmed = confirmed.groupby('Country/Region', as_index=False)
confirmed = confirmed.sum()
deaths = pd.read_csv(jhu_link_deaths)
deaths = deaths.iloc[:, 1:]
deaths = deaths.groupby('Country/Region', as_index=False)
deaths = deaths.sum()

# Using the following list, we will create different plots
countries = ['Spain', 'France', 'Colombia', 'United Kingdom', 'Israel']
# The following empty dataset will contain all the integrated data set after processing data
covid_data = pd.DataFrame(columns=['date', 'cases', 'kind', 'country'])


# To prepare the data there are three steps
# i. filter the countries to consider
# ii. transpose the dataframe and set dates as row values
# iii. set the country name as column name and delete the first three rows (names and coordinates)
confirmed_countries = confirmed[confirmed['Country/Region'].isin(countries)]
confirmed_countries = confirmed_countries.T.reset_index()
confirmed_countries.columns = confirmed_countries.iloc[0]
confirmed_countries = confirmed_countries.iloc[3:]
confirmed_countries['kind'] = 'confirmed cases'

# The same process is applied to deaths data set
deaths_countries = deaths[deaths['Country/Region'].isin(countries)]
deaths_countries = deaths_countries.T.reset_index()
deaths_countries.columns = deaths_countries.iloc[0]
deaths_countries = deaths_countries.iloc[3:]
deaths_countries['kind'] = 'deaths'

# We merge the two datasets considering the confirmed cases as the main dataset
data_countries = confirmed_countries.append(deaths_countries)
# Also, we adjust the column names
data_countries = data_countries.rename(columns={'Country/Region': 'date'})
# To work with dates, we need to transform a data type to
data_countries['date'] = pd.to_datetime(data_countries['date'])

# To define the facet grid we set two columns as a reference
# The first one comes from the year and month to report
data_countries['year_month'] = data_countries['date'].dt.to_period('M')
data_countries['day'] = data_countries['date'].dt.day
# The second one comes from the country
g = sns.FacetGrid(data_countries, row='kind', col='year_month', margin_titles=False)
g.map(sns.scatterplot, 'day', 'Colombia', color='#334488', size=0.1)
g.map(sns.scatterplot, 'day', 'Spain', color='#004488', size=0.1)

plt.show()
plt.close()

print('End')