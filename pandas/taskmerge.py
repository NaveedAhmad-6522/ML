import pandas as pd

students = pd.DataFrame({
    "Students_ID": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Sara", "Usman", "Zara", "Ahsan"],
    "Department": ["CS", "IT", "CS", "EE", "EE"]
})

fees = pd.DataFrame({
    "ID": [1, 2, 4, 6],
    "Fee_Paid": [3000, 3500, 2500, 2700]
})

'''
✅ Task 1:

Merge the students and fees DataFrames on the ID columns, and show only the students who paid fees.


⸻'''
merge1=pd.merge(students,fees, left_on='Students_ID',right_on='ID')
print(merge1)

'''

✅ Task 2:

Do a left join to see all students, and show whether they paid fees (use a new column "Fee_Paid"). Fill unpaid rows with 0.



⸻'''

leftjoin = pd.merge(students, fees, left_on='Students_ID', right_on='ID', how="left")
leftjoin["Fee_Paid"] = leftjoin["Fee_Paid"].fillna(0)
print(leftjoin)

'''

✅ Task 3:

Do a full outer join, and count how many students or fee entries do not have matches (i.e., show rows with missing values).'''

fullouter=pd.merge(students,fees, left_on='Students_ID',right_on='ID' ,how='outer')
print(fullouter)

unmatched=fullouter[fullouter.isnull().any(axis=1)]
print(unmatched)



df1 = pd.DataFrame({
    "Name": ["Zara", "Ahsan"],
    "Score": [75, 82]
}, index=["A", "B"])

df2 = pd.DataFrame({
    "Grade": ["B", "A"]
}, index=["A", "C"])

# Merge using index (outer join)

result=pd.merge(df1,df2,left_index=True,right_index=True, how='outer')
print(result)
result1=df1.join(df2,how='outer')
print(result1)