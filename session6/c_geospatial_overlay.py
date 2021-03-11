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
#import mapclassify
#import pyproj
#from pyproj import Proj
from shapely.geometry import Point, Polygon



# We read the file from Open Data Barcelona
# the columns of the DataFrame
# https://opendata-ajuntament.barcelona.cat/data/en/dataset/20170706-districtes-barris/resource/cd800462-f326-429f-a67a-c69b7fc4c50a
bcn_admin_areas = geopandas.read_file('../data/0301100100_UNITATS_ADM_POLIGONS.json')
bcn_census_areas = bcn_admin_areas[bcn_admin_areas['TIPUS_UA'] == 'SEC_CENS']

# We get a testing data set for drawing points
foot_fall = pd.read_csv('../data/Footfall_data_python.csv')

#foot_fall.columns
#Index([u'ID', u'X', u'Y'], dtype='object')
foot_fall['geometry'] = foot_fall.apply(lambda row: Point(row.LONGITUDE, row.LATITUDE), axis=1)
foot_fall_gdf = geopandas.GeoDataFrame(foot_fall)

# We can plot individual layers
ax = bcn_census_areas.boundary.plot()
ax.set_title("Barcelona Administrative Areas")
plt.show()

# Second plot
ax1 = foot_fall_gdf.plot()
print('End')


# to overlay the two layers we need to be sure they share the common CRS
# In order to get a projected view of our plots, we need to change the CRS first
bcn_census_areas = bcn_census_areas.to_crs({'init': 'epsg:4326'})

# Later, we need to define the base layers and the overlay
base = bcn_census_areas.plot(color='white', edgecolor='black')

foot_fall_gdf.plot(ax=base, marker='o', color='red', markersize=5)

print('End')
