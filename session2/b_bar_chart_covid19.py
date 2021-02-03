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

# First, we will create bar plots for a country
country = countries[0]
title = 'COVID-19 %s' % country
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


covid_data = confirmed_data.append(deaths_data)
covid_data['year_month'] = covid_data['date'].dt.to_period('M')

ax = sns.barplot(x='year_month', y='cases', hue='kind', data=covid_data, ci=None)
ax.set(xlabel='Year - Month', ylabel='Cases', title=title)
plt.show()
plt.close()




# Not sure if this code below works properly

data = deaths_data[deaths_data['deaths'] > 0]
initial_day = data['date'].min()
data['day'] = data['date'] - initial_day
data['day'] = data['day']/np.timedelta64(1, 'D')
ax = sns.lineplot('day', 'deaths', data=data)
ax.set(xlabel='Days after first case detected', ylabel='Deaths', title=title)
plt.show()
plt.close()

# Second, We will compare two variables using scatterplot
country_data = pd.merge(confirmed_data, deaths_data)
ax = sns.scatterplot('confirmed_cases', 'deaths', data=country_data)
ax.set(xlabel='Confirmed cases', ylabel='Deaths', title=title)
plt.show()
plt.close()


# Third, we can also use density plots here
# density plots refer to the following documentation
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0#:~:text=Density%20Plots%20in%20Seaborn&text=The%20curve%20shows%20the%20density,scale%20as%20the%20density%20plot.
# Density Plot and Histogram of all arrival delays
sns.distplot(country_data['deaths'], hist=True, kde=True,
             bins=100, color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
plt.show()
plt.close()

print('Compare multiple countries and analyse')
print('Try to create integrate multiple plots per country')