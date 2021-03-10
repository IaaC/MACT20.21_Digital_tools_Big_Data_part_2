# encoding: utf-8

##################################################
# This script shows uses the pandas library to create statistically describe datasets
# It also shows basic plotting features
# Find extra documentation about data frame here:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot libraries matplotlib and seaborn
import pandas as pd
import geopandas
import matplotlib.pyplot as plt


# We read the file from Open Data Barcelona
# https://opendata-ajuntament.barcelona.cat/data/en/dataset/20170706-districtes-barris/resource/cd800462-f326-429f-a67a-c69b7fc4c50a
bcn_admin_areas = geopandas.read_file('../data/0301100100_UNITATS_ADM_POLIGONS.json')

# In order to get a projected view of our plots, we need to change the CRS first
# bcn_admin_areas = bcn_admin_areas.to_crs({'init': 'epsg:2169'})

# PRINT OUT a basic plot with municipalities
ax = bcn_admin_areas.plot()
ax.set_title("Barcelona Administrative Areas")
plt.show()

print('End')
