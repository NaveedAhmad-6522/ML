student_number=int(input("enter Student Number"))


def grade_calculator(marks):
 if marks<0 or marks>100:
  print("Marks Should be inbetween 1 ,100")

 elif marks>90:
  print("you passed!")
  print("Grade A")

 elif marks>80 and marks<90:
  print("you passed!")
  print("Grade B")


 elif marks>70 and marks<80:
  print("you passed!")
  print("Grade C")

 elif marks>60 and marks<70:
  print("you passed!")
  print("Grade D")

 else:
  print("you passed!")
  print("Grade F")

for i in range(student_number):
    student_name=input("Enter Name:")
    student_marks=float(input("Enter  Marks"))
    print(f"hello ,{student_name}")
    grade_calculator( student_marks)
