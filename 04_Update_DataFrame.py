import pandas as pd

df = pd.read_csv('IRIS.csv')
print(df)

df.at[2:4,'sepal_length'] = [2,4,6] #for single element to update
#print(df.head(4))

#adding new column
df['age'] = list(range(0,150))
print(df.head())