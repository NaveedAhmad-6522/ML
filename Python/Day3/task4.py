students=[]

for i in range(5):
    name , marks =input(f"enter {i+1} student name and marks i.e. Naveed 67.232: ").split()
    students.append({"name":name, "marks":float(marks)})


with open("student.txt", "w") as file1:
    for i in students:
     file1.write(f"{i['name']} , {i['marks']}\n")