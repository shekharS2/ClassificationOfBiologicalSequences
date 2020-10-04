import pandas as pd

df = pd.read_csv('k-gap-PCA123.csv', header=None)
print(df)

ds = df.sample(frac=1)
print(ds)

ds.to_csv('k-gap-PCA-shuffled123.csv')