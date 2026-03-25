import pandas as pd

data = {
    'carat':[0.23,0.21,0.23,0.29,0.31],
    'cut':['Ideal','Premium','Good','Premium','Good'],
    'color':['E','E','E','I','J'],
    'price':[326,326,327,334,335],
    'x':[3.95,3.89,4.05,4.20,4.34],
    'y':[3.98,3.84,4.07,4.23,4.35],
    'z':[2.43,2.31,2.31,2.63,2.75]
}

df = pd.DataFrame(data)

# i) Mean price for each cut
print("Mean price:\n", df.groupby('cut')['price'].mean())

# ii) Count of diamonds
print("\nCount:\n", df.groupby('cut')['price'].count())

# Min & Max price
print("\nMin price:\n", df.groupby('cut')['price'].min())
print("\nMax price:\n", df.groupby('cut')['price'].max())

# Average of x, y, z
print("\nAverage x:", df['x'].mean())
print("Average y:", df['y'].mean())
print("Average z:", df['z'].mean())
