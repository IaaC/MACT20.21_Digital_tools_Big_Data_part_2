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

# Using the following list, we will create a set of plots
countries = ('Spain', 'France', 'Colombia', 'United Kingdom')

# The following empty dataset will contain all the integrated data set after processing data
covid_data = pd.DataFrame(columns=['date', 'cases', 'kind', 'country'])

# Through a loop, we extract the values per country,
# merge the results from the two datasets and
# append the integrated data to a single dataset
for country in countries:
    # Preparing data from confirmed cases
    confirmed_country = confirmed[confirmed['Country/Region'] == country]
    if len(confirmed_country) > 0:
        confirmed_data = confirmed_country.groupby('Country/Region', as_index=False)
        confirmed_data = confirmed_data.sum()
        confirmed_data = confirmed_data.iloc[:, 4:]
        confirmed_data = confirmed_data.T
        confirmed_data = confirmed_data.reset_index()
        confirmed_data.columns = ['date', 'cases']
        confirmed_data['date'] = pd.to_datetime(confirmed_data['date'])
        confirmed_data['kind'] = 'confirmed'
        confirmed_data['country'] = country

    # Preparing data from death cases
    deaths_country = deaths[deaths['Country/Region'] == country]
    if len(deaths_country) > 0:
        deaths_data = deaths_country.groupby('Country/Region', as_index=False)
        deaths_data = deaths_data.sum()
        deaths_data = deaths_data.iloc[:, 4:]
        deaths_data = deaths_data.T
        deaths_data = deaths_data.reset_index()
        deaths_data.columns = ['date', 'cases']
        deaths_data['date'] = pd.to_datetime(deaths_data['date'])
        deaths_data['kind'] = 'deaths'
        deaths_data['country'] = country

    # Building a dataset for the country that includes confirmed and death cases
    covid_country = confirmed_data.append(deaths_data)
    covid_data = covid_data.append(covid_country)


covid_data['year_month'] = covid_data['date'].dt.to_period('M')

g = sns.FacetGrid(covid_data, col='country', hue='kind')
g.map(sns.barplot, 'year_month', 'cases', ci=None)

plt.show()
plt.close()

print('End')