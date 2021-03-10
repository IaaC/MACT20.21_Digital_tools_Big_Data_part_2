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
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# We read the file from Open Data Barcelona
# https://opendata-ajuntament.barcelona.cat/data/en/dataset/20170706-districtes-barris/resource/cd800462-f326-429f-a67a-c69b7fc4c50a
bcn_admin_areas = geopandas.read_file('../data/0301100100_UNITATS_ADM_POLIGONS.json')
bcn_census_areas = bcn_admin_areas[bcn_admin_areas['TIPUS_UA'] == 'SEC_CENS']
# We are converting the census area code from text to integers
bcn_census_areas.loc[:, 'ca_code'] = pd.to_numeric(bcn_census_areas['SEC_CENS'])

# In order to get a projected view of our plots, we need to change the CRS first
# bcn_admin_areas = bcn_admin_areas.to_crs({'init': 'epsg:2169'})

# We then prepare the writer and animation file options
Writer = animation.writers['ffmpeg']
writer = Writer(fps=1, metadata=dict(artist='MaCTResearcher'), bitrate=1800)

fig = plt.figure()
fig.set_size_inches(10, 6)
frames = bcn_census_areas['ca_code'].max()


# The second one returns a line (sin function) based on a parameter
def animate(i):
    frame_data = bcn_census_areas[bcn_census_areas['ca_code'] <= i]
    frame_data.plot()
    plt.title("Barcelona Census Areas")
    plt.show()


# Lastly,the animation function uses the previous parameters to produce multiple plots
danim = FuncAnimation(fig, animate, frames=frames)
anim.save('geospatial_animation.mp4', writer=writer)




print('End')

# Merging data and plotting two elements
# prepare population data, merge with countries data frame and get a subset of columns

# For more than one country, and more than one variable, there are options to arrange subplots
# Merge data from Lux

pop_selection = pop[['Year', '1821', '1900', '2001', '2020']]
pop_selection.columns = ['commune', 'pop_1821', 'pop_1900', 'pop_2001', 'pop_2020']
mplts_pop = pd.merge(mplts, pop_selection, left_on='COMMUNE', right_on='commune', how='left')
# geodataframes demands special treatment. Default merge options look like the following:
# selection = mplts.merge(pop_selection, on='name', how='left').dropna()


# Set up the visual outputs using subplots for map and legend elements
fig, ax = plt.subplots(1, 1)
# Additional schemas come from "mapclassify" library
mplts_pop[mplts_pop['pop_2020'].isna() == False].plot(column='pop_2020', ax=ax, cmap='magma', scheme='fisher_jenks', legend=True)
ax.set_title("Luxembourg Population. Year 2020")
ax.set_axis_off()
plt.show()
# There are options for saving plots
# plt.savefig('../outcomes/map_pop.png', dpi=300, format='png')




# How about multiple plots
# prepare population data, merge with countries data frame and get a subset of columns
# SET UP THE VISUAL OUTPUT
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4)
# SET THE FIRST MAP
mplts_pop[mplts_pop['pop_1821'].isna() == False].plot(column='pop_1821', ax=ax1, cmap='magma', scheme='fisher_jenks', legend=False)
ax1.set_axis_off()
# SET THE SECOND MAP
mplts_pop[mplts_pop['pop_1900'].isna() == False].plot(column='pop_1900', ax=ax2, cmap='magma', scheme='fisher_jenks', legend=False)
ax2.set_axis_off()
# SET THE THIRD MAP
mplts_pop[mplts_pop['pop_2001'].isna() == False].plot(column='pop_2001', ax=ax3, cmap='magma', scheme='fisher_jenks', legend=False)
ax3.set_axis_off()
# SET THE FOURTH MAP
mplts_pop[mplts_pop['pop_2020'].isna() == False].plot(column='pop_2020', ax=ax4, cmap='magma', scheme='fisher_jenks', legend=True)
ax4.set_axis_off()
ax.set_axis_off()
plt.show()
# There are options for saving plots
# plt.savefig('../outcomes/map_gdp.png', dpi=300, format='png')

# You might have issues of cartographic projections
# PRINT THE COORDINATE REFERENCE SYSTEM ATTRIBUTE
print(mplts_pop.crs)

# CHANGE COORDINATES REFERENCE SYSTEM FROM a: epsg 1234 TO b: 4567 (IMPORTANT TO INSTALL PYPROJ LIBRARY VERSION 2.2.0)
mplts_pop = mplts_pop.to_crs({'init': 'epsg:2169'})
ax = mplts_pop.plot()
ax.set_title("Luxembourg")
plt.show()