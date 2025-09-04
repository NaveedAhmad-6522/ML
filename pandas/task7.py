import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)
'''.	Load the dataset into a DataFrame.
	2.	Print:
	•	Number of rows and columns
	•	Column names
	•	Data types of each column
	3.	Show:
	•	First 10 rows
	•	Last 5 rows
	4.	Get a summary of numerical columns (describe())
	5.	Print the mean fare and median age
	6.	Show how many unique values are in:
	•	Embarked
	•	Sex
	•	Pclass
	7.	Use .value_counts() to count:
	•	How many male and female passengers?
	•	How many people embarked from each port?
	8.	Print the index (passenger ID) of the person who paid the highest fare.
	9.	Bonus: What is the name of the passenger who is oldest?

    ''''''
print("number of rows and columns respectivly",df.shape)
print("Columns names",df.columns.tolist())
print("data type of each columns",df.dtypes)
print("first 10 rows",df.head(10))
print("last 5 rows",df.tail())
print("summery: ",df.describe())
print("mean  , fare ,age ",df["Fare"].mean(),df["Age"].median())
print("Unique values in Embark , Sex,Pclass :",df["Embarked"].nunique(),df["Sex"].nunique(), df["Pclass"].nunique())
print("male and female Passengers",(df["Sex"]=="Male").value_counts(),(df["Sex"]=="Female").value_counts())
print("People Embarked from each port",df["Embarked"].value_counts())
print("index",df["Fare"].max)
print("oldest",df["Age"].max)
'''
import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1. Number of rows and columns
print("1. Number of rows and columns:", df.shape)

# 2. Column names
print("\n2. Column names:\n", df.columns.tolist())

# 3. Data types of each column
print("\n3. Data types:\n", df.dtypes)

# 4. First 10 rows
print("\n4. First 10 rows:\n", df.head(10))

# 5. Last 5 rows
print("\n5. Last 5 rows:\n", df.tail(5))

# 6. Summary of numerical columns
print("\n6. Summary statistics:\n", df.describe())

# 7. Mean fare and median age
print("\n7. Mean Fare:", df["Fare"].mean())
print("   Median Age:", df["Age"].median())

# 8. Unique values in Embarked, Sex, Pclass
print("\n8. Unique values:")
print("   Embarked:", df["Embarked"].nunique())
print("   Sex:", df["Sex"].nunique())
print("   Pclass:", df["Pclass"].nunique())

# 9. Count of male and female passengers
print("\n9. Male & Female passenger counts:\n", df["Sex"].value_counts())

# 10. People embarked from each port
print("\n10. Embarked counts:\n", df["Embarked"].value_counts(dropna=False))

# 11. Index of person who paid the highest fare
highest_fare_index = df["Fare"].idxmax()
print("\n11. Index of passenger who paid highest fare:", highest_fare_index)

# 12. Name of the oldest passenger
oldest_age_index = df["Age"].idxmax()
oldest_name = df.loc[oldest_age_index, "Name"]
print("12. Oldest passenger's name:", oldest_name)