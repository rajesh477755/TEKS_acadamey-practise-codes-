import statistics as st
import pandas as pd

data = {
  'name': ["alice", "david", "bob", "eve", "charlie"],
  'age': [25, 25, 30, 33, 23],
  'gender': ["female", "nan", "male", "female", "mlae"],
  'salary': [50000, 60000, 0, 45000, 55000]
}
df = pd.DataFrame(data)
print(df)
mean_s = df['salary'].mean()
mean_a = df['age'].mean()
print(mean_a)
print(mean_s)
df['salary'].fillna(mean_s, inplace=True)
df['age'].fillna(mean_a, inplace=True)
df.loc[1, 'gender'] = 'male'
print(df)