import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Usman", "Zara", "Ahsan", "Mona", "Tariq", "Nida"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["CS", "CS", "EE", "CS", "EE", "EE", "CS", "EE"],
    "Marks": [88, 92, 85, 75, 91, 79, 68, 95],
    "Fee": [3000, 3500, 2800, 2600, 3200, 2700, 2500, 3600]
}

df = pd.DataFrame(data)

'''	1.	Group by Gender and show average Marks.
	2.	Group by Department and get max and min of Marks.
	3.	Group by both Gender and Department, and find average Fee.
	4.	Use .agg() to get multiple stats (mean, max) of Marks per Department.
	5.	Reset the index after a groupby and return the result as a DataFrame.
    6.  Show the average Marks and Fee for each Department, and sort them by average Marks (descending).
    '''
print("Average marks: ",df.groupby("Gender")["Marks"].mean())
print("Departmental marks min:",df.groupby("Department")["Marks"].min())
print("Departmental marks max:",df.groupby("Department")["Marks"].max())
print("Departmental marks max & min :\n",df.groupby("Department")["Marks"].agg(["max","min"]))
print("group by Gender and department and  avergae fee: \n",df.groupby(["Gender","Department"])["Fee"].mean())
print("Departmental marks max & Mean :\n",df.groupby("Department")["Marks"].agg(["max","mean"]))
print(df.groupby(["Name","Marks"])["Fee"].mean().reset_index())
print(df.sort_values(["Marks", "Fee"], ascending=False).reset_index())
grouped=df.groupby(["Name","Marks"])["Department"].first().reset_index()
print(grouped.sort_values("Name"))