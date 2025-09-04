import pandas as pd

# First DataFrame
students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Zara", "Usman"]
})

# Second DataFrame
fees = pd.DataFrame({
    "ID": [1, 2, 4, 5],
    "Fee": [3000, 3500, 2500, 2700]
})


merged=pd.merge(students,fees, on='ID')
print(merged)


leftmerged=pd.merge(students,fees, on='ID' , how="left")
print(leftmerged)

rightmerged=pd.merge(students,fees, on='ID' ,how="right")
print(rightmerged)

outermerged=pd.merge(students,fees, on='ID' ,how="outer")
print(outermerged)