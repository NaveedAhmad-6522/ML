import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#1. Show only the first 7 passengers’ Name, Sex, and Age using .loc.

print(df.loc[0:6,["Name","Age","Sex"]])
''' Get the Name and Fare of the passenger with index 150 using .loc.

🔹 3. List passengers whose Fare is more than 50 and Pclass is 1 or 2.'''

print(df.loc[150,["Name","Fare"]])

print(df[(df["Fare"]>50) & (df["Pclass"].isin(['1','2']))]) 

print("Name start with M and female",df[(df["Name"].str.startswith("M") & (df["Sex"]=="Female"))])

print("pessanger embaerked from  Queenstown", df[df["Embarked"].isin(["Q"])])

'''show only the Name and Age of passengers who:

	•	Are older than 60, and
	•	Paid less than 30'''

print(df[(df["Age"]>60) & (df["Fare"]<30)])

#List all unique embarkation ports and how many passengers from each.
print(df["Embarked"].unique())
print(df["Embarked"].value_counts())