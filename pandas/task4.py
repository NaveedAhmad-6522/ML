import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.iloc[5:11])
print(df.iloc[25:31])

print(df.loc[99,"Name"])

'''

    1.  Print rows with label 5 to 10 using loc.
	2.	Print the age and fare of the passenger with index label 50.
	3.	Use loc to print names of passengers between index 15 and 20.

⸻
'''
print(df.loc[5:9])
print(df.loc[50,["Fare","Age"]])
print(df.loc[16:19,"Name"])
print("null count:",df.info())
print(df.describe())