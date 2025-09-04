url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
import pandas as pd
df=pd.read_csv(url)
columnsa=df.columns
print("Columns", df.columns)
print(df.head)
print(df.tail)
print(df.shape)