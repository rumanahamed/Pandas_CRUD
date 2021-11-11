import pandas as pd

df = pd.read_csv('Iris1.csv') # it will print all the data from the csv file
print(df)
df = pd.read_csv('Iris1.csv').head() #it will will top 5 data from the file
print(df)
df = pd.read_csv('Iris1.csv').tail() #it will print bottom 5 data from the file
print(df)