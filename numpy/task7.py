import numpy as np
np.random.seed(42)
marks =np.random.randint(40,100,size=20)
print("Student array",marks)
grading_assigning=np.where(marks>=90,"A",
                    np.where(marks>=80,"B",
                    np.where(marks>=70,"C",
                    np.where(marks>=60,"D","F"))))
gradeAB=(grading_assigning=="A") |( grading_assigning=="B")
print(gradeAB)
print("A ,B Grades",marks[gradeAB])
print("failed students position: ", np.where(marks<60)[0])

failedstudents=sum(marks<=59)
print("Unique marks",np.unique(marks))
print(grading_assigning)
print("failed",failedstudents)



values=np.linspace(0,1 ,10)
print(values) 
values1=np.linspace(100,200,5,endpoint=False)
print(values1)
values3=np.linspace(0,2*np.pi,5)
print(values3)