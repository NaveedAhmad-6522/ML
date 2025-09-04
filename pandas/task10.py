import pandas as pd
import numpy as np

'''df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Usman", "Zara"],
    "Age": [25, None, 30, None],
    "Fare": [100, 85, None, None]
})
1.	Age with the mean age
	2.	Fare with the value 0
	3.	Show the updated DataFrame

df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

df["Fare"].fillna(0,inplace=True)
print(df)

'''

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Usman", None, "Zara", "Ahsan"],
    "Age": [25, None, 30, None, 29, None],
    "Fare": [100, 85, None, None, 90, None],
    "City": [None, "Lahore", None, "Peshawar", None, None]
})
'''
	1.	Fill Age column with its mean.
	2.	Fill Fare column with 0.
	3.	Fill City column using forward fill (ffill).
	4.	Now reset everything and re-do Step 3 with bfill instead of ffill.
     '''
df1=df.copy()
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Fare"].fillna(0,inplace=True)
df2=df1
df1["City"].fillna(method="ffill",inplace=True)
df3=df2
df3["City"].fillna(method="bfill",inplace=True)

df3.fillna({"Age": 99, "Fare": -1, "City": "Unknown"}, inplace=True)#dictionay filling
