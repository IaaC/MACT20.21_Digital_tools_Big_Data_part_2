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

# We need to import numpy and matplotlib library
# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import matplotlib

# Read files and prepare data
data = pd.read_csv('../data/2021_seguiment-covid19-bcn.csv')
#data = pd.read_csv('https://opendata-ajuntament.barcelona.cat/data/dataset/4f3ffbda-d5be-4f2a-a836-26a77be6df1a/resource/f627ac0a-d05f-416d-9773-eeb464a3fc44/download')
data.columns = ['date_indicator', 'frequency_indicator', 'place', 'name_indicator',
                'name_variable', 'value', 'unit', 'source']
# data comes with multiple indicators, we need to pick just one of it for our initial plot
data = data[data['name_indicator'] == 'Casos de COVID-19 a Barcelona (diari)']
# We need the data to be in time format to calculate values in days after day zero
data['date_indicator'] = pd.to_datetime(data['date_indicator'])
initial_day = data['date_indicator'].min()
data['day_after_zero'] = data['date_indicator'] - initial_day
data['day_after_zero'] = data['day_after_zero']/np.timedelta64(1, 'D')
# we also extract some values to set the plot limits
max_day = data['day_after_zero'].max().astype(int)
max_cases = data['value'].max()
title = 'Covid-19 cases BCN'

# We then prepare the writer and animation file options
Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='MaCTResearcher'), bitrate=1800)
# If error using anaconda try to install ffmpeg
# conda install -c conda-forge ffmpeg

# We create an initial plot with basic configuration a single line
fig = plt.figure(figsize=(10, 6))
plt.xlim(0, max_day)
plt.ylim(0, max_cases)
plt.xlabel('Day after case 1', fontsize=18)
plt.ylabel('Cases', fontsize=18)
plt.title(title, fontsize=20)


# We need to set an animation function to handle individual behaviour per frame
# variable "i" is the frame id that can be used to handle queries or filters for your data
def animate(i):
    frame_data = data[data['day_after_zero'] <= i]
    p = sns.lineplot(x='day_after_zero', y='value', data=frame_data, color="r")
    p.tick_params(labelsize=17)
    plt.setp(p.lines, linewidth=1)


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=max_day, repeat=True)
ani.save('covid_cases_bcn.mp4', writer=writer)
print('end')
