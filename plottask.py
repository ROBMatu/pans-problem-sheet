# plottask.py
# Author: Robert O'Brien-Monk
# A histogram of a normal distribution of a 1000 values,
# with a mean of 5 and standard deviation of 2.
# And a plot of the function  h(x)=x3 in the range [0, 10]
# sources:
# https://www.w3schools.com/python/matplotlib_labels.asp
# https://www.w3schools.com/python/matplotlib_line.asp
# https://www.w3schools.com/python/matplotlib_grid.asp
# https://matplotlib.org/stable/gallery/color/named_colors.html

import numpy as np
import matplotlib.pyplot as plt

# Histogram of normal distribution of 1000 values, mean of 5 and standard deviation of 2
normdata = np.random.normal(loc= 5, scale= 2, size = 1000)
plt.hist(normdata, color='firebrick')

# lineplot of function h(x)=x3
xpoints = np.array(range(0,10))
hpoints = xpoints ** 3
plt.plot(xpoints,hpoints,label = "h(x)=x3", color='navy', linewidth= '3')

# Plot Style
font= {'family':'Times','color':'indigo', 'size':20}
subfont = {'family':'Times','color':'firebrick', 'size':15}

plt.title("Normal Distribution and h(x)=x3", fontdict=font)
plt.xlabel("h(x) value", fontdict=subfont)
plt.ylabel("x cubed", fontdict=subfont)
plt.legend()
plt.grid(color = 'black', linestyle = 'dotted', linewidth = 0.25)

# Displays the plot
plt.show()