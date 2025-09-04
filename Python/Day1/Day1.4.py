students = [
    {"name": "Naveed", "marks": 88},
    {"name": "Basit", "marks": 65},
    {"name": "Omar", "marks": 40},
    {"name": "Jamal", "marks": 95},
    {"name": "Haris", "marks": 72}
]

# Step 2: Add grade to each student
def assign_grade(marks):
    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    elif marks > 70:
        return "C"
    elif marks > 60:
        return "D"
    else:
        return "F"

students.sort(key=lambda s:s["marks"], reverse=True)


for student in students:
    student["Grade"]=assign_grade(student["marks"])


print(students)

mylist=[12,34,5,32,245]
above100=len([m for m in mylist if m>100])

newlist=(m for m in mylist if m>100)
for i in newlist:
    print(i)
print(above100)