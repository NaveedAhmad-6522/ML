import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Ahmed', 'Sara', 'Ayesha'],
    'Gender': ['Male', 'Male', 'Female', 'Female']
})

print("Original DataFrame:")
print(df)

# Apply get_dummies
df_encoded = pd.get_dummies(df, columns=['Gender'])

print("\nAfter One-Hot Encoding:")
print(df_encoded)

df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)
print(df_encoded)


df1 = pd.DataFrame({
    'City': ['Lahore', 'Peshawar', 'Karachi'],
    'Education': ['BS', 'MS', 'BS']
})

df_encoded = pd.get_dummies(df1)
print(df_encoded)


'''task
	•	🔹 Use pd.get_dummies() to one-hot encode the columns Gender, City, and Subject.
	•	🔹 Also use drop_first=True to avoid multicollinearity (drop one dummy column per category).
	•	🔹 Concatenate the encoded columns back with the Name column.
	•	🔹 Final DataFrame should contain:
	•	Name
	•	Dummy columns for Gender, City, and Subject.


'''

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Zaid'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Karachi'],
    'Subject': ['Math', 'Biology', 'Physics', 'Math', 'Biology']
}

df2 = pd.DataFrame(data)
print(df2)
df_encoded1=pd.get_dummies(df2,columns=['Gender','City','Subject'],drop_first=True,dtype=int)
print(df_encoded1)


df3= pd.DataFrame({
    'City': ['Lahore', 'Karachi', 'Peshawar'],
    'Weather': ['Hot', 'Hot', 'Cold']
})

df3.replace({
    'City': {'Lahore': 'LHR', 'Karachi': 'KHI'},
    'Weather': {'Hot': 1, 'Cold': 0}
}, inplace=True)

print(df3)



df4 = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Male', 'Female']
})

# Replace values using map
df4['Gender_Code'] = df4['Gender'].map({'Male': 1, 'Female': 0})
print(df4)