import pandas as pd

df = pd.read_csv('IRIS.csv')
print(df.head())

df.drop(['sepal_length','petal_length'],axis=1,inplace=True)
print(df.head())
