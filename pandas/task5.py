import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
#rows and columns
'''print(df.shape)
print(df.columns)
print("3 rows",df.iloc[0:2,:])


print("columns wiht name age sex ",df.loc[:,["Name","Age","Sex"]])
print(df.iloc[50,:])
print(df.loc[100,["Name","Fare"]])'''

print(df[df["Name"]=="Female"])
print(df[df["Age"]<=16])
print(df[df["Name"].str.startswith("A")])



