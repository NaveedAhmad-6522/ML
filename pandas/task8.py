import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.isnull().sum())   # Total missing values per column

print(df.notnull().sum())
dropeed=df.dropna(axis=1)
print(dropeed)
