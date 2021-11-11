import pandas as pd

df = pd.read_csv('IRIS.csv')
#print(df.head(10))
# select particular column
#df[column name]-----selection based on column name
single_column = df['sepal_length'].head() # head function will help to extract top 5 data from csv file.
print(single_column)
print(type(single_column))
single_column1 = df['sepal_length'].tail()
print(single_column1)
print(type(single_column1))

#selection of rows
single_row = df['sepal_length'][0:5]
print(single_row)


