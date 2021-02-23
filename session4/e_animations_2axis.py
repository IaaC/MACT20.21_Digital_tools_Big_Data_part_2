# encoding: utf-8

##################################################
# This script shows how to create animated plots using matplotlib and a basic dataset
# Multiple tutorials inspired the current design but they mostly came from:
# hhttps://towardsdatascience.com/how-to-create-animated-graphs-in-python-bb619cc2dec1
# Note: the project keeps updating every course almost yearly
##################################################
#
##################################################
# Author: Diego Pajarito
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
# We need to import numpy and matplotlib library
# importing libraries
import pandas as pd
import seaborn as sns

# Read files and prepare data
data = pd.read_csv('../data/2021_seguiment-covid19-bcn.csv')
#data = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/4f3ffbda-d5be-4f2a-a836-26a77be6df1a/resource/f627ac0a-d05f-416d-9773-eeb464a3fc44/download')
data.columns = ['date_indicator', 'frequency_indicator', 'place', 'name_indicator',
                'name_variable', 'value', 'unit', 'source']
# We will use two datasets to generate plots
data_daily = data[data['name_indicator'] == 'Casos de COVID-19 a Barcelona (diari)']
data_accumulated = data[data['name_indicator'] == 'Casos de COVID-19 a Barcelona (acumulat)']

# We need the data to be in time format to calculate values in days after day zero
data_daily.loc[:, 'date_indicator'] = pd.to_datetime(data_daily['date_indicator'])
initial_day = data_daily['date_indicator'].min()
data_daily.loc[:, 'day_after_zero'] = data_daily['date_indicator'] - initial_day
data_daily.loc[:, 'day_after_zero'] = data_daily['day_after_zero']/np.timedelta64(1, 'D')
# We need the data to be in time format to calculate values in days after day zero
data_accumulated.loc[:, 'date_indicator'] = pd.to_datetime(data_accumulated['date_indicator'])
data_accumulated.loc[:, 'day_after_zero'] = data_accumulated['date_indicator'] - initial_day
data_accumulated.loc[:, 'day_after_zero'] = data_accumulated['day_after_zero']/np.timedelta64(1, 'D')

# we also extract some values to set the plot limits
max_day = data_daily['day_after_zero'].max().astype(int)
max_cases_daily = data_daily['value'].max()
max_cases_accumulated = data_accumulated['value'].max()
title = 'Barcelona: '

# We then prepare the writer and animation file options
Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='MaCTResearcher'), bitrate=1800)
# If error using anaconda try to install ffmpeg
# conda install -c conda-forge ffmpeg

# We create an initial plot with basic configuration a single line
fig, ax1 = plt.subplots()
fig.set_size_inches(10, 6)
plt.title(title + 'Covid-19 cases', fontsize=18)
plt.xlabel('Day after case 1', fontsize=14)
plt.ylim(0, max_cases_accumulated)
plt.ylabel('Accumulated', fontsize=18)

# # now we configure the secondary axis
ax2 = ax1.twinx()
plt.ylim(0, max_cases_daily*2)
cases_ticks = np.arange(0, max_day, 50)


# We need to set an animation function to handle individual behaviour per frame
# variable "i" is the frame id that can be used to handle queries or filters for your data
def animate(i):
    frame_data_daily = data_daily[data_daily['day_after_zero'] <= i]
    frame_data_accumulated = data_accumulated[data_accumulated['day_after_zero'] <= i]
    sns.lineplot(x='day_after_zero', y='value', data=frame_data_accumulated, color="r", ax=ax1)
    sns.barplot(x='day_after_zero', y='value', data=frame_data_daily, color='b', ax=ax2)
    plt.ylabel('Daily', fontsize=18)
    plt.xlim(0, max_day)
    plt.xticks(cases_ticks)
    plt.xlabel('Day after case 1', fontsize=18)
    # Handling secondary axis implies different management in the animate function


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=max_day, repeat=True)
ani.save('covid_cases_bcn_2axis.mp4', writer=writer)
print('end')
