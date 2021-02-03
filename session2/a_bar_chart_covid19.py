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
countries = ('Spain', 'France', 'Colombia', 'United Kingdom')

# First, we will create a bar plot for a single country
# cumulative daily cases per country
country = countries[0]
title = 'COVID-19 %s' % country
confirmed_country = confirmed[confirmed['Country/Region'] == country]
if len(confirmed_country) > 0:
    confirmed_data = confirmed_country.groupby('Country/Region', as_index=False)
    confirmed_data = confirmed_data.sum()
    confirmed_data = confirmed_data.iloc[:, 4:]
    confirmed_data = confirmed_data.T
    confirmed_data = confirmed_data.reset_index()
    confirmed_data.columns = ['date', 'confirmed_cases']
    confirmed_data['date'] = pd.to_datetime(confirmed_data['date'])
data = confirmed_data[confirmed_data['confirmed_cases'] > 0]
initial_day = data['date'].min()
data['day'] = data['date'] - initial_day
data['day'] = data['day']/np.timedelta64(1, 'D')
ax = sns.barplot(x='day', y='confirmed_cases', data=data)
ax.set(xlabel='Days after first case detected', ylabel='Confirmed cases', title=title)
plt.show()
plt.close()


# Second, we can group some values to make the plot easy to read
data['year_month'] = data['date'].dt.to_period('M')
ax = sns.barplot(x='year_month', y='confirmed_cases', data=data, ci=False)
ax.set(xlabel='Year / month', ylabel='Confirmed cases', title=title)
plt.show()
plt.close()

print('end')