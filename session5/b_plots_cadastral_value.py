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
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/b1c57236-9d41-4aef-b103-ef1f21da285c/resource/a792417e-d7e2-40d9-aba6-15e1f388e266/download/2020_loc_hab_sup_mitjana.csv'
residential_areas = pd.read_csv(url)
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/b1c57236-9d41-4aef-b103-ef1f21da285c/resource/a1394695-81fe-4788-b3b3-88f76229b693/download/2019_loc_hab_sup_mitjana.csv'
residential_areas_temp = pd.read_csv(url)
residential_areas = residential_areas.append(residential_areas_temp)
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/b1c57236-9d41-4aef-b103-ef1f21da285c/resource/6c4cbaa3-c4f0-4591-a1e0-c163b5540a7c/download/2018_loc_hab_sup_mitjana.csv'
residential_areas_temp = pd.read_csv(url)
residential_areas = residential_areas.append(residential_areas_temp)
# Data from year 2017 generates error, we ommited this data set for the example
# url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/b1c57236-9d41-4aef-b103-ef1f21da285c/resource/14693be4-53f7-4c03-91a9-2b4fdd21d8ed/download/2017_sup_mitjana_habitatge.csv'
# residential_areas_temp = pd.read_csv(url)
# residential_areas = residential_areas.append(residential_areas_temp)

# Let's start with a simple histogram for data from 2020
sns.histplot(data=residential_areas, x="Sup_mitjana_m2")
plt.close()

# After multiple iterations we can generate a more readable plots - Lines
sns.histplot(data=residential_areas, x="Sup_mitjana_m2", hue='Any', stat='density', element='poly')
plt.close()

# And also bars
sns.histplot(data=residential_areas, x="Sup_mitjana_m2", hue='Any', multiple='dodge', binwidth=5, stat='density')
plt.close()