import pandas as pd
import numpy as  np
data = {
    'Name': ['Alice', 'Bob', 'Bob', 'David', 'Eva', 'Bob', None],
    'Age': [25, 25, 25, -1, 22, 25, 30],
    'Gender': ['F', 'M', 'M', 'Male', 'F', 'M', None],
    'Salary': [50000, 60000, np.nan, 40000, None, 60000, 45000],
    'JoinDate': ['2021-01-01', '2021-07-20', '2020/03/15', None, '2022-10-10', '2021-07-20', '2021-07-20']
}
df=pd.DataFrame(data)
#finding duplicate

duplicates = df[df.duplicated()]
duplicates1=df[df.duplicated(subset=['Name','Age'])]

print(duplicates1)
print(duplicates)

#droping

df_no_duplicate=df.drop_duplicates()
print(df_no_duplicate)

'''reseting the index plus removing via columns'''
df_no_duplicate1=df.drop_duplicates(subset=['Name','Age']).reset_index(drop=True)
print("\nDROPING\n",df_no_duplicate1)