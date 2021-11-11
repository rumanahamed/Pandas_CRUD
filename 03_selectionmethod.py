import pandas as pd

df = pd.read_csv('IRIS.csv')
#by label - loc method

result = df.loc[0]
print(result)

# accessing multiple row and one column
result1 = df.loc[0:3,['sepal_length']]
print(result1)

# accessing multiple row and multiple column
result1 = df.loc[0:3,'sepal_length':'sepal_width'] #we can also pass 2nd argument in square bracket[] seperated by comma(,)
print(result1)

df1 = df.head()
print(df1,type(df1))
df1.set_index('sepal_length',inplace=True)
print(df1)
result2 = df1.loc[5.1:4.6,'sepal_width':'petal_width']
print(result2)

result3 = df1.loc[4.6,'petal_length'] # scaler value/only 1 value from the datasheet.
print(result3)

#at method is also used to print scaler value
result4 = df1.at[4.6,'petal_length']
print(result4)

#ILOC method also known as selection by position
result5 = df.iloc[3]
print('ILOC=',result5)

result6 = df.iloc[1:3,0:2] #i represnt integer
print(result6)

result7 = df.iloc[[1,3,5],[1,3]] #it will print 1,3,5 row data and 1,3 column value
print(result7)

result8 = df.iat[1,2] #iat method is also used to print scaler value but argument passed are integer having row and column.
print(result8)

print(df.index)
new_index = list(range(150,301))
print(new_index)
df.set_index(new_index,inplace=True)
print(df.head)