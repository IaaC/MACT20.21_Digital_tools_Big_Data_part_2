# encoding: utf-8

##################################################
# This script shows how to create animated plots using matplotlib and a basic dataset
# Multiple tutorials inspired the current design but they mostly came from:
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
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
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


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
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


# Lastly,the animation function uses the previous parameters to produce multiple plots
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

#
anim.save('sine_wave.gif', writer='imagemagick')
