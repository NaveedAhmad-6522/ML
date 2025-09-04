import pandas as pd
import numpy as np

# Create dirty dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Bob', None],
    'Age': [25, np.nan, 35, -1, 22, 25, 30],
    'Gender': ['F', 'M', 'M', 'Male', 'F', 'M', None],
    'Salary': [50000, 60000, np.nan, 40000, None, 60000, 45000],
    'JoinDate': ['2021-01-01', 'not_available', '2020/03/15', None, '2022-10-10', '2021-07-20', '2021-07-20']
}

df = pd.DataFrame(data)
print(df)
nullinmae=df.count()
print(nullinmae)
droping=df.dropna(subset=['Age','Name'])
print("Dropped\n",droping)

missingagefilling=df.fillna(df['Age'].mean())
missingagefilling=missingagefilling.replace(-1,df['Age'].mean())
missingagefilling=missingagefilling.replace("Male","M")

print(missingagefilling)