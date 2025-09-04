'''import numpy as np

marks=np.random.randint(40,100,500)
reshaped=marks.reshape(5,100)
TotalMarksPerStudent=np.sum(reshaped,axis=0)
print(TotalMarksPerStudent)
AverageMarksPerClass=np.sum(TotalMarksPerStudent)/len(TotalMarksPerStudent)
Heighest=np.max(TotalMarksPerStudent)
Lowest=np.min(TotalMarksPerStudent)



grades=np.where(reshaped>=90,"A",
        np.where(reshaped>=80,"B",
        np.where(reshaped>=70,"C",
        np.where(reshaped>=60,"D","F"))))

gradeForEachStudent=grades.T

for idx, row in enumerate(gradeForEachStudent):
    print(f"Student {idx+1}: {'  '.join(row)}")
'''


import numpy as np

# Step 1: Generate marks and reshape
marks = np.random.randint(40, 100, 500)
reshaped = marks.reshape(5, 100)  # 5 subjects × 100 students

# Step 2: Calculate total and average
TotalMarksPerStudent = np.sum(reshaped, axis=0)   # (100,)
AverageMarksPerClass = np.mean(TotalMarksPerStudent)
Highest = np.max(TotalMarksPerStudent)
Lowest = np.min(TotalMarksPerStudent)

# Step 3: Assign grades per subject
grades = np.where(reshaped >= 90, "A",
         np.where(reshaped >= 80, "B",
         np.where(reshaped >= 70, "C",
         np.where(reshaped >= 60, "D", "F"))))  # shape: (5, 100)

gradeForEachStudent = grades.T  # (100, 5)

# Step 4: Print each student's grades
print("\n📋 Grades Report:\n")
# Assuming gradeForEachStudent is shape (100, 5)
student_id = 1  # Start from student 1

for row in gradeForEachStudent:
    print(f"Student {student_id}: {' '.join(row)}")
    student_id += 1  # Manually increment the counter
# Step 5: Topper
topper_index = np.argmax(TotalMarksPerStudent)
print(f"\n🏆 Topper: Student {topper_index + 1} with {TotalMarksPerStudent[topper_index]} marks")

# Step 6: Grade Distribution
print("\n📊 Grade Distribution:")
unique_grades, counts = np.unique(grades, return_counts=True)
for g, c in zip(unique_grades, counts):
    print(f"Grade {g}: {c} times")

# Step 7: Failed Students (at least one F)
failed_mask = np.any(grades == "F", axis=0)
failed_students = np.where(failed_mask)[0]
print(f"\n❌ Students who failed at least one subject: {len(failed_students)}")
print("Failed Student IDs:", failed_students + 1)

# Step 8: Summary
print(f"\n📈 Class Average (Total Marks): {AverageMarksPerClass:.2f}")
print(f"Highest Total: {Highest}")
print(f"Lowest Total: {Lowest}")