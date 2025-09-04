import pandas as pd

data = {
    'Name': ['Alice', 'Naveed', 'Zarar', 'David', 'Eva'],
    'Marks': [88, 92, 85, 75, 91]
}

df = pd.DataFrame(data)
print(df)

# Apply len function to each Name
df['Name_length'] = df['Name'].apply(len)
print(df)

def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(grade)
print(df)

# Add 5 bonus marks to each student
df['Bonus_Marks'] = df['Marks'].apply(lambda x: x + 5)
print(df)

# Apply row-wise function (needs axis=1)
df.apply(lambda row: row['Marks'] + len(row['Name']), axis=1)
print(df)

