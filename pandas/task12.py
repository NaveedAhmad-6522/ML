import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Usman", "Zara", "Ahsan", "Mona", "Tariq", "Nida", "Ali", "Zara"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["CS", "CS", "EE", "CS", "EE", "EE", "CS", "EE", "CS", "CS"],
    "Marks": [88, 92, 85, 75, 91, 79, 68, 95, 88, 75],
    "Fee": [3000, 3500, 2800, 2600, 3200, 2700, 2500, 3600, 3000, 2600]
}

df = pd.DataFrame(data)
'''	1.	Group by Gender and show the average Marks.
	2.	Group by Department and return the min and max Marks.
	3.	Group by both Gender and Department, and show the average Fee.
	4.	Group by Department and use .agg() to get:
	•	Mean and max of Marks
	•	Total Fee paid (hint: use "Fee": "sum" in .agg)
	5.	Show the average Marks and Fee for each Department, sorted by average Marks descending.
	6.	Group by Name and Marks, and return the first Department. Then sort by Name and Marks.
	7.	Bonus 🔥: Find the student(s) who paid the highest fee.'''

print("Grouped by Gender, average Marks \n",df.groupby("Gender")["Marks"].mean())
print("Grouped by departemnt min and max:\n",df.groupby("Department")["Marks"].agg(["min","max"]))
print("Grouped by both Gender and Department, average Fee \n",df.groupby(["Gender","Department"])["Fee",].mean())
print("Grouped by departemnt mean and max total Fee Paid:\n",df.groupby("Department")["Fee"].agg(["mean","max","sum"]))
print("Average Marks and fee for each department : ",df.groupby("Department")[["Marks","Fee"]].mean().sort_values(["Marks","Fee"],ascending=False))
print("Grouped by Name and Marks, and return the first Department and  sorted by Name and Marks",df.groupby(["Name","Marks"])["Department"].first().reset_index().sort_values(["Name","Marks"],ascending=False))
max_fee = df["Fee"].max()
print("Student(s) with highest fee:\n", df[df["Fee"] == max_fee])

''' What’s Remaining (To Master Pandas for ML):

🔷 1. Grouping and Aggregation
	•	groupby() with agg() to summarize data
	•	Example: df.groupby('Gender')['Salary'].mean()

🔷 2. Sorting and Ranking
	•	sort_values(), sort_index()
	•	rank() to rank values within groups

🔷 3. Data Transformation
	•	apply() with lambda functions
	•	map(), applymap()
	•	pipe() for chaining transformations

🔷 4. Date and Time Handling
	•	pd.to_datetime()
	•	.dt accessor to extract year, month, day, etc.
	•	Filtering by date ranges

🔷 5. Pivot Tables and Crosstab
	•	pivot_table() for multi-level aggregation
	•	pd.crosstab() for frequency tables

🔷 6. Merging, Joining, and Concatenating
	•	merge() for SQL-style joins
	•	concat() to stack dataframes vertically or horizontally
	•	join() method

🔷 7. Window Functions / Rolling Statistics
	•	rolling().mean(), expanding().sum()
	•	Useful for time-series and trend analysis

🔷 8. Binning and Categorization
	•	cut() and qcut() to convert continuous values into bins
	•	.astype('category') for categorical optimization

🔷 9. Dealing with Outliers
	•	IQR or Z-score method to detect/filter outliers
	•	Visual inspection using boxplots with Seaborn

🔷 10. Data Export
	•	to_csv(), to_excel(), to_json()

⸻

💡 Extra (Recommended for ML):
	•	Feature Engineering with Pandas:
	•	Extracting features from text, date, numeric
	•	Creating new columns based on logic
	•	Memory Optimization:
	•	Downcasting data types to reduce memory usage

⸻

🔁 Lets Continue:

Do you want to go in order from the remaining topics (like GroupBy ➝ Sorting ➝ Transformations…)
or
Would you like to jump directly to a specific topic youre curious about?

Lets keep going step by step 🚀'''