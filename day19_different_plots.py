import matplotlib.pyplot as plt
import numpy as np
'''
Differemnt types of plots 
I) plot:
This is noraml type of plotting of a graph using points and lines
II) Scatter 
This is a way of plotting the graph with only plotting the points in the graph and leaving them alone with out connecting them
This can be done by using scatter() function 
arguments that are used in scatter plot 
1) color: this is used to set color to the points in the graph 
we can use color code or color refernece or color map which can also show colour bar for the color map that we are using or an array of colors for reference to what color to use at what point in the graph
2)size: 
This is used to give size to the points which can be fixed or can be chnaged by using array of sizes for reference 
3)Alpha:
This is used to control the transparencey of the points '''
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
'''
III)Bar graph
This is a way of plotting graphs using Bars as represention  
There are two types of bar graph representation 
1)bar
this gives us vertical bar plots 
this can be done by using bar() function 
2)barh
this gives us horizontal bar plots 
this can be done by using barh() function 
Arguments that can be used in bar() and barh() function 
1)color:
this gives the bar a color that we want 
Arguments that can be used in bar() function 
1)width:
this gives bar a width that we want to be in 
Arguments that can be used in barh()
1)height:
this gives bar a height that we want to be in 
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y, height=0.1, color='r')
plt.show()
plt.bar(x, y, width=0.1, color='r')
plt.show()
'''
IV)Histogram 
this is a type of graph that is used for showing frequency distribution 
this can be done by using hist() function '''
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
'''
V) Pie chart 
this is a type of graph where we divide a circle into parts for illusatrating data 
this can be done by using pie () function 
Arguments in pie() fucntion 
1)labels
this is used to give labels to the slices in the pie chart 
2)Start angle 
This gives the chart a start angle by which it will start plotting the graph 
3)Explode
this will pop out a particular slice of the chart with reference to the distance array we give 
4)Shadow 
This will give the poped out slice a shadow effect 
5)Color: 
this is used to set color to the points in the graph 
we can use color code or color refernece or color map which can also show colour bar for the color map that we are using or an array of colors for reference to what color to use at what point in the graph
6)legend:
This will give us a small list consisting of labels and their respective colors
'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y,
        labels=mylabels,
        startangle=90,
        explode=myexplode,
        shadow=True,
        colors=mycolors)
plt.legend(title='Four fruits:')
plt.show()
'''
VI)Plot box
 It is a type of chart that depicts a group of numerical data through their quartiles. It is a simple way to visualize the shape of our data. It makes comparing characteristics of data between categories very easy.
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')
plt.show()
'''
VII)Pseudocolor mesh
This is a type of ploting that shows us values of 2D array using colors using color mapping '''
from pandas import DataFrame
import matplotlib.pyplot as plt

data = [{2, 3, 4, 1}, {6, 3, 5, 2}, {6, 3, 5, 4}, {3, 7, 5, 4}, {2, 8, 1, 5}]
Index = ['I1', 'I2', 'I3', 'I4', 'I5']
Cols = ['C1', 'C2', 'C3', 'C4']
df = DataFrame(data, index=Index, columns=Cols)

plt.pcolor(df)
plt.show()
'''
VIII)3d chart 
'''