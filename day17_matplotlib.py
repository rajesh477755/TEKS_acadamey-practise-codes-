'''matplotlib is a python library which is used for data visualisation created by John D Hunter 
For using this we need to import either numpy or pandas library for data handling 
We can install matplotlib using pip keyword '''
import matplotlib.pyplot as plt
import numpy as np
'''operations using pyplot '''
'''pyplot means python ploting which is used to plot the data we given as input into graphs of ourchoice and cosutomisation '''
#ploting
#we use plot fucntion for this operation
x = np.array([0, 6])
y = np.array([0, 25])
plt.plot(x, y)
plt.plot(x)
plt.plot(y)
'''the output of the above functions is a graph which is plotted using x,y values '''
plt.plot(x, y, 'o')
'''the output of the above function is a graph where there will be a circle marker placed in every point plotted in the graph which is called as marker'''
'''there are many types of markers the we can use for marking the values in the graph for using them we can use marker reference as parameter '''
'''Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline	
'''
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title("graph")
''' tha above functions will name the sides and the graph that we have plotted '''
plt.show()
'''the above function will print the graph in the output'''
plt.plot(y, 'o:r')
'''the above function will plot a graph using y values and mark values with cicle nad plot them using a red dotted '''
'''there are many types of line that we can use for plotting by giving line refernce as parameter in plot function '''
'''The marker value can be anything from the Marker Reference above.

The line value can be one of the following:

Line Reference
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'Dashed line	
'-.'Dashed/dotted line'''
'''there are may colors we can use for plotting the graph by giving color reference as parmeter in plot function '''
'''color reference:
r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White'''
plt.show()
