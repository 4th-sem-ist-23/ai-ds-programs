import pandas as pd


df = pd.DataFrame({
	"A" : [23, 12, 4, 2, 7]
})

print(df)
print(df.info())
print(df.describe())
print(df.notnull())
print(df.min())
print(df.max())
print(df.var())
print(df.std())
print(df.mean())
print(df.median())
print(df.sum())
print(df.count())
