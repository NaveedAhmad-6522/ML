import pandas as pd
import numpy as  np
data = {
    'Name': ['Alice', 'Bob', 'Bob', 'David', 'Eva', 'Bob', None],
    'Age': [25, 25, 25, -1, 22, 25, 30],
    'Gender': ['F', 'male', 'M', 'Male', 'Female', 'M', None],
    'Salary': [50000, 60000, np.nan, 40000, None, 60000, 45000],
    'JoinDate': ['2021-01-01', '2021-07-20', '2020/03/15', None, '2022-10-10', '2021-07-20', '2021-07-20']
}
df=pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())
df_cleaned1=df.dropna()
print(df_cleaned1)
df_cleaned = df.dropna(subset=['Salary', 'JoinDate'])
print(df_cleaned)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['JoinDate']=df['JoinDate'].fillna(method='ffill') 

df['Gender'] = df['Gender'].str.lower()  # all lowercase
df['Gender'] = df['Gender'].replace({
    'male': 'M',
    'female': 'F',
    'f': 'F',
    'm': 'M'
})
df['Age'] = df['Age'].replace(-1, np.nan)
print(df)

