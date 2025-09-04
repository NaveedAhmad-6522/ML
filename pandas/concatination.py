import pandas as pd
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Ali", "Sara"]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Usman", "Zara"]
})

df3 = pd.DataFrame({
    "ID": [5, 6],
    "Name": ["Ahsan", "Hira"]
})

'''
🚀 Task 1:

👉 Concatenate all three dataframes vertically.
👉 Reset the index.

🚀 Task 2:

👉 Concatenate the same three dataframes column-wise.
👉 Try using keys=["DF1", "DF2", "DF3"] to identify columns.
'''
result=pd.concat([df1,df2,df3],ignore_index=True)
print(result)

result1=pd.concat([df1,df2,df3],keys=["df1","df2","df3"],axis=1)
print(result1)
print("\n",result1["df1"]["Name"])

