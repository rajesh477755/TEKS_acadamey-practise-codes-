'''pandas is a library in python that is used for handling datasets'''
#syntax for installing pandas
#pip install pandas
import pandas as pd
''' in pandas we will mainly operate on dictionaries which is a data type which consists of key and value pair '''
'''Syntax 
  dictonary_name={'key1':values,'key2:value2'}
  In dictionary every value must have a key but every key dosnet need a value'''
df = {'days': [1, 2, 3, 4], 'calories': [30, 40, 50, 60]}
#operations using dictionary
#1)dataframe
'''This gives dictionary as output but in form of rows and columns '''
x = pd.DataFrame(df)
print(x)
#2)Index
'''this can either used for getting the values in the data set (or) used for modifiying the index of the data set '''
x2 = pd.DataFrame(df, index=["day1", "day2", "day3", "day4"])
print(x2)
#3) Series
'''this is  column in a table that is used as a data set'''
a = [1, 2, 3, 4, 5]
x3 = pd.Series(a)
print(x3)
'''this print the serires as a data set '''
#4)Labels
'''this is a way of acessing the values in the data set '''
print(x3[0])
#5) Location
'''this is a way of finding what data is there in a particaular position and return it as Key value pair '''
print(x.loc[[0, 1, 2]])
