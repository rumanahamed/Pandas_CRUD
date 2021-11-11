import pandas as pd
df = pd.read_csv('Iris1.csv')
#accessing column
# display = df['SepalLengthCm']
# print(display)
# display = df['SepalLengthCm'].head()
# print(display)
# display = df['SepalLengthCm'].tail()
# print(display)
# display = df[:].describe()
# print(display)

#accessing rows
display1 = df[:][5:15]
print(display1)
