# encoding: utf-8

##################################################
# This script shows how to create animated plots using matplotlib and a basic dataset
# Multiple tutorials inspired the current design but they mostly came from:
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# Data uses the Open Data Barcelona API and especially the dataset
#
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
import urllib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import pandas as pd
import matplotlib
plt.style.use('seaborn-pastel')


# Data access through Open Data BCN API
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/d3b744a6-fc21-4375-a043-9eb7299c11c9/resource/1b6ff879-134f-4ff6-be09-81d1c30678a1/download/2020_carrec_valors.csv'
cadastral_values = pd.read_csv(url)
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/b1c57236-9d41-4aef-b103-ef1f21da285c/resource/a792417e-d7e2-40d9-aba6-15e1f388e266/download/2020_loc_hab_sup_mitjana.csv'
residential_areas = pd.read_csv(url)


# Let's start with a simple histogram
sns.histplot(data=cadastral_values, x="Valor_€")


# First we set a variable to store the figure with fixed axis configuration
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)


# Also, we need two main functions to build the animation
# The first one returns an empty line
def init():
    line.set_data([], [])
    return line,


# The second one returns a line (sin function) based on a parameter
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = x * x * 0.01 * i
    line.set_data(x, y)
    return line,


# Lastly,the animation function uses the previous parameters to produce multiple plots
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

#
anim.save('sine_wave.gif', writer='imagemagick')
