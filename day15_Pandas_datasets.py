'''Operations on data sets '''
#1)Importing a file
import pandas as pd

df = pd.read_csv('BankCustomers (1).csv')
print(df)
#2)Convereting whole data into string
'''for this method we will use .to_string() method '''
print(df.to_string())
#3)Reading data
'''for reading a part of the data in the data set we can use head() or tail() and we can also get certrain no of records in that data set '''
print(df.head())
print(df.tail())
print(df.head(10))
print(df.tail(10))
#4)Getting informaation about the data set
'''for this we will use info() function '''
print(df.info())
#5) droping
'''this will drop a particaluar data in that data set for this we will use dropna() function'''
new_df1 = df.dropna()
df.dropna(inplace=True)
print(new_df1)
print(df)
#6) Filling null values
'''this will help us to fill us some data in null spaces in the data set for this we will use fillna()'''
df.fillna(130, inplace=True)
df["Gender"].fillna("N/A", inplace=True)
print(df)
#7) finding location of a particular data
''' this will help us to find a particular set of data in the dataset for this we will use loc[] function '''
df.loc[0, "Job Classification"] = "other"
print(df)
#8) duplication
''' this will copy the entire data set and print it once it is recvoked for this we will use duplicate() function '''
print(df.duplicated())
'''by using same function we can drop dulpicate values in a data set by using adding drop keyword '''
print(df.drop_duplicates())
