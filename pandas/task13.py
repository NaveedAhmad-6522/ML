import pandas as pd

students = pd.DataFrame({
    'Student_ID': [1, 2, 3, 4],
    'Name': ['Ali', 'Sara', 'Usman', 'Zara']
})

marks = pd.DataFrame({
    'Student_ID': [2, 4, 3, 1],
    'Marks': [87, 92, 76, 88]
})

# Merge based on Student_ID
result=pd.merge(students,marks,  on ='Student_ID')
print(result)
mergedleft=pd.merge(students,marks, on ='Student_ID' , how='left')
print(mergedleft)