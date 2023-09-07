#arguments we can use in plot function
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='H', ms=30, mec='r', linewidth='10')
plt.show()
#marker size (ms)
#this is usesd to assign a size for the marker that we are using
#marker edge color (mec)
#this is used to give a color to edege of the marker
#marker face color (mfc)
#this is used to give a colour to the marker that we use
#linewidth
#this is used to assign some width to the line that is used for ploting the graph
plt.plot(ypoints, marker='H', ms=30, mec='r', linewidth='10')
plt.grid()
#this is used for getting grid lines in the background of the graph
#parameters that we can use in graph function
plt.show()
plt.plot(ypoints, marker='H', ms=30, mec='r', linewidth='10')
plt.grid(color='green', linestyle='--', linewidth=0.8)
plt.show()
plt.plot(ypoints, marker='H', ms=30, mec='r', linewidth='10')
plt.grid(axis='x', color='green', linestyle='--', linewidth=0.8)
plt.show()
plt.plot(ypoints, marker='H', ms=30, mec='r', linewidth='10')
plt.grid(axis='y', color='green', linestyle='--', linewidth=0.8)
plt.show()
#color
#this is used to assign a color to the grid line in the background
#linestyle
#this is used to assign a line style to the grid lines in the background
#line width
#this is used to assign a width to the grid lines in the background
'''Display Multiple Plots
for this subplot() function is used draw multiple plots in one figure:'''
#syntax subplot(no.of rows,no.of columns,position of that plot in that plotting matrix)
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y)
#plot 3 :
x = np.array([0, 1, 2, 3])
y = np.array([23, 40, 70, 50])
plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.show()