'''
Task Steps:
	1.	Create a DataFrame with at least 5 students, with columns:
	•	'Name'
	•	'Marks'
	2.	Sort the DataFrame by 'Marks' in descending order.
	3.	Show the DataFrame after sorting (observe the index).
	4.	Then:
	•	✅ Use reset_index() and print the result.
	•	✅ Use reset_index(drop=True) and print the result.
	•	✅ Finally, use sort_index() and show the output.

⸻

✅ Bonus (optional):
	•	Add a 'Grade' column based on 'Marks' (e.g., A for ≥90, B for ≥80, etc.)
	•	Show how the index plays a role after sorting and resetting.
    '''

import pandas as pd
data={
     'Name': ['Alice', 'Naveed', 'zarar', 'David', 'Eva'  ],
     'Marks': [88, 92, 85, 75, 91]
}
df=pd.DataFrame(data)
df=df.sort_values(['Name','Marks'], ascending=True)
print(df)
print(df)
df=df.sort_index()
print(df)