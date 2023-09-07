import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('50_Startups.csv')
df = pd.DataFrame(data)
print(df)
'''Exploratory data analysis'''
print('Head')
print(df.head())
print("Tail")
print(df.tail())
print("Information")
print(df.info())
print('Shape')
print(df.shape)
print('Data types')
print(df.dtypes)
print('Columns')
print(df.columns)
print('index')
print(df.index)
print('describe')
print(df.describe)
print(df['State'].describe)
print('is null')
print(df.isnull)
print(df.isnull().sum())
print('mean')
print(df['Administration'].mean())
print(df.groupby(['Administration', 'Marketing Spend'])['Profit'].mean())
print('mode')
print(df['Administration'].mode())
print('median')
print(df['R&D Spend'].median())
print('rename')
print(df.rename(columns={'State': "Location"}))
print('groupby')
print(df.groupby('Marketing Spend')['Profit'].min())
print('drop null values')
print(df.dropna())
'''
Seaborn 
This is a library which is used for making statistical graphics in python which helps us explore and understand data in python 
There are many types of graphs in seaborn
1)Count plot 
It is used to visuvalize the count of categiorical variables 
this can be done by using countplot() function
arguments in count plot 
x, y: This parameter take names of variables in data or vector data, optional, Inputs for plotting long-form data.
hue : (optional) This parameter take column name for colour encoding.
data : (optional) This parameter take DataFrame, array, or list of arrays, Dataset for plotting. If x and y are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.
order, hue_order : (optional) This parameter take lists of strings. Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.
orient : (optional)This parameter take “v” | “h”, Orientation of the plot (vertical or horizontal). This is usually inferred from the dtype of the input variables but can be used to specify when the “categorical” variable is a numeric or when plotting wide-form data.
color : (optional) This parameter take matplotlib color, Color for all of the elements, or seed for a gradient palette.
palette : (optional) This parameter take palette name, list, or dict, Colors to use for the different levels of the hue variable. Should be something that can be interpreted by color_palette(), or a dictionary mapping hue levels to matplotlib colors.
saturation : (optional) This parameter take float value, Proportion of the original saturation to draw colors at. Large patches often look better with slightly desaturated colors, but set this to 1 if you want the plot colors to perfectly match the input color spec.
dodge : (optional) This parameter take bool value, When hue nesting is used, whether elements should be shifted along the categorical axis.
ax : (optional) This parameter take matplotlib Axes, Axes object to draw the plot onto, otherwise uses the current Axes.
kwargs : This parameter take key, value mappings, Other keyword arguments are passed through to matplotlib.axes.Axes.bar()
'''
print('count plot')
sns.countplot(x='R&D Spend', data=df)
plt.show()
'''
2)Scatter plot
It is used to show the relation between two numerical values 
Arguments in Scatter plot
x, y: Input data variables that should be numeric.

data: Dataframe where each column is a variable and each row is an observation.

size: Grouping variable that will produce points with different sizes.

style: Grouping variable that will produce points with different markers.  

palette: Grouping variable that will produce points with different markers.  

markers: Object determining how to draw the markers for different levels.

alpha: Proportional opacity of the points.
'''
sns.scatterplot(x='R&D Spend', y='State', data=df)
plt.show()
'''
3)Barplot
It is used to compare the values of different categories 
x, y, 
hue	names of variables in “data“ or vector data, optional	Inputs for plotting long-form data. See examples for interpretation.
data	
DataFrame, array, or list of arrays, optional	Dataset for plotting. If “x“ and “y“ are absent, this is interpreted as wide-form. Otherwise it is expected to be long-form.
order, hue_order	
lists of strings, optional	Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.
estimator	
callable that maps vector -> scalar, optional	Statistical function to estimate within each categorical bin.
ci	
float or “sd” or None, optional	Size of confidence intervals to draw around estimated values.  If “sd”, skip bootstrapping and draw the standard deviation of the observations. If “None“, no bootstrapping will be performed, and error bars will not be drawn.
n_boot	
int, optional	Number of bootstrap iterations to use when computing confidence intervals.
units	
name of variable in “data“ or vector data, optional	Identifier of sampling units, which will be used to perform a multilevel bootstrap and account for repeated measures design. 
orient	
“v” | “h”, optional	Orientation of the plot (vertical or horizontal). This is usually inferred from the dtype of the input variables, but can be used to specify when the “categorical” variable is a numeric or when plotting wide-form data.
color	
matplotlib color, optional	Color for all of the elements, or seed for a gradient palette.
palette	
palette name, list, or dict, optional	Colors to use for the different levels of the “hue“ variable. Should be something that can be interpreted by :func:`color_palette`, or a dictionary mapping hue levels to matplotlib colors.
saturation	
float, optional	Proportion of the original saturation to draw colors at. Large patches often look better with slightly desaturated colors, but set this to “1“ if you want the plot colors to perfectly match the input color spec.
errcolor	
matplotlib color	Color for the lines that represent the confidence interval.
errwidth	
float, optional	Thickness of error bar lines (and caps). 
capsize	float, optional	Width of the “caps” on error bars.
dodge	
bool, optional	When hue nesting is used, whether elements should be shifted along the categorical axis. 
ax	
matplotlib Axes, optional	Axes object to draw the plot onto, otherwise uses the current Axes.
kwargs	
ey, value mappings	Other keyword arguments are passed through to “plt.bar“ at draw time.
'''
sns.barplot(x='R&D Spend', y='State', data=df)
plt.show()
sns.boxplot(x='employment_type', y='salary', data=df)
plt.show()
sns.stripplot(x='remote_ratio', y='company_size', data=df)
plt.show()
