import numpy as np
# 1. Generate marks
np.random.seed(42)
marks = np.random.randint(40, 100, size=20)
print("🎯 Marks:", marks)

# 2. Assign grades using np.where()
grades = np.where(marks >= 90, "A",
         np.where(marks >= 80, "B",
         np.where(marks >= 70, "C",
         np.where(marks >= 60, "D", "F"))))
print("📄 Grades:", grades)

# 3. Boolean indexing: A or B
ab_mask = (grades == "A") | (grades == "B")
print("🏆 A or B grades:", marks[ab_mask])

# Count how many failed
fail_count = np.sum(grades == "F")
print("❌ Failed students:", fail_count)

# 4. Clip marks between 50 and 95
curved_marks = np.clip(marks, 50, 95)
print("🧪 Curved Marks:", curved_marks)

# 5. Unique grades
unique_grades = np.unique(grades)
print("🔠 Unique Grades:", unique_grades)

# 🔧 Bonus: any/all checks
print("🧐 Any score < 60?", np.any(marks < 60))
print("✅ All scores >= 50?", np.all(marks >= 50))

curved=np.clip(marks,45,70)
print("curved",curved)
print("any", np.any(marks>10))
print("all",np.all(marks>50))


arr = np.array([[1, 89, 3],
                [3, 456, 2]])

max_index=np.argmax(arr)
print(max_index)
print("2D array max index: ",np.unravel_index(max_index,arr.shape))
print(arr.shape)