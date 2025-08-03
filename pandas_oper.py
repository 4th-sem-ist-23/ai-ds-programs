import pandas as pd
import numpy as np

data = {"A" : [10, 15, 18, 21, 25]}
df = pd.DataFrame(data)
print("Data Frame")
print(df)

print("Sum of each column : ")
print(df.sum())
print("Mean of a each column : ")
print(df.mean())
print("Median of a each column : ")
print(df.median())
print("Mode of a each column : ")
print(df.mode())
print("Minimum value of each column : ")
print(df.min())
print("Maximumn value of each column : ")
print(df.max())
print("Count of non-null values of each column")
print(df.count())
print("Variance of each column")
print(df.var())
print("Standard deviation of each column")
print(df.std())

