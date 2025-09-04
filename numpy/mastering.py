import numpy as np
from functools import reduce
np.random.seed(42)
marks=np.random.randint(40,100,50)
reshapedwithoutnormalized=marks.reshape(10,5)
reshaped=np.clip(reshapedwithoutnormalized,50,90)
TotalMarksForStudent=np.sum(reshaped,axis=1)

AverageMarks=np.mean(TotalMarksForStudent)
Topper=np.argmax(TotalMarksForStudent)
Lowest=np.argmin(TotalMarksForStudent)
grade=np.where(reshaped>=90,"A",
      np.where(reshaped>=80,"B",
      np.where(reshaped>=70,"C",
      np.where(reshaped>=60,"D","F"))))


for index,grading in enumerate(grade):
    print(f"Student ID {index+1} :{' '.join(grading)}")


atleast1F=np.any(grade=="F",axis=1)
print(atleast1F)
failedstudensindices=np.where(atleast1F)
print(failedstudensindices[0]+1)
gradesoccurance,count=np.unique(grade,return_counts=True)
zipping=zip(gradesoccurance,count)
print(zipping)
for g,c in zipping:
        print(f"Grade {g}: {c} times")


studentpassedall=np.all(grade!="F",axis=1)
passedcom=np.where(studentpassedall)
print("student id passed all ",passedcom[0]+1)

max=TotalMarksForStudent[0]
for i in TotalMarksForStudent:
      if (i==max):
            print()
unique,number=np.unique(TotalMarksForStudent,return_counts=True)
zipping=zip(unique,number)
for c,n in zipping:
      print(f"Marks {c} : {n} Times")

zipping = list(zip(unique, number))  # ✅ make reusable
for c,n in zipping:
      print(np.where(TotalMarksForStudent==c)[0])