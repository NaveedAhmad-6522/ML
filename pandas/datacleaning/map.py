import pandas as pd

df = pd.DataFrame({
    'Grade': ['A', 'B', 'C', 'A', 'B']
})

grade_map = {'A': 4.0, 'B': 3.0, 'C': 2.0}
df['GPA'] = df['Grade'].map(grade_map)

print(df)

df['GPA+Bonus'] = df['GPA'].map(lambda x: x + 0.5)
print(df)


import pandas as pd

df = pd.DataFrame({
    'Math': [87, 45, 99],
    'English': [78, 64, 88]
})

# Add 5 bonus marks to each subject
df_bonus = df.applymap(lambda x: x + 5)

print(df_bonus)