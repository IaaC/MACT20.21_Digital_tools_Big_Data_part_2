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

# Let's start with a simple histogram
sns.histplot(data=cadastral_values, x="Valor_€")
plt.close()

# We cal also see the different alternatives to visualise histograms and frequencies
# A histogram with pre-defined bin-widths for 50k €
sns.histplot(data=cadastral_values, x="Valor_€", binwidth=50000000)
plt.close()
# Histograms per district
sns.histplot(data=cadastral_values, x="Valor_€", hue='Nom_districte')
plt.close()
# Different histograms per district and pre-defined bin-widths
sns.histplot(data=cadastral_values, x="Valor_€", binwidth=100000000, hue='Nom_barri')
plt.close()
# Histograms using lines/steps or polygons
sns.histplot(data=cadastral_values, x="Valor_€", hue='Nom_districte', element="step")
plt.close()
sns.histplot(data=cadastral_values, x="Valor_€", hue='Nom_districte', element="poly")
plt.close()



# 2D histograms
sns.histplot(data=cadastral_values, x="Valor_€", y='Nom_districte')
plt.close()

print('End')
