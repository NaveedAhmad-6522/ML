import numpy as np
 
np.random.seed(42)
marks=np.random.randint(50,100, size=10)
heightst=np.max(marks)
lowest=np.min(marks)
meanvalue=np.mean(marks)
studentabove90=np.sum(marks>=90)

sorted_marks=(np.sort(marks))[::-1]


print("Marks:", marks)
print("Highest Mark:", heightst)
print("Lowest Mark:", lowest)
print(f"Average Mark: {meanvalue:.2f}")
print("Number of students scoring ≥ 90:", studentabove90)