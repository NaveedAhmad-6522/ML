students_number=int(input("enter the number of students: "))

students=[]
for i in range(students_number):

    name ,marks=input("enter name and marks ").split()
    students.append({"name":name, "marks":float(marks)})

with open("marks.txt","w") as file1:
    for line in students:
        file1.write(f"{line['name']} {line['marks']:.2f} \n")

loadingstudents=[]
with open("marks.txt" , "r") as file2:
    for line in file2:
        name , marks = line.strip().split()
        loadingstudents.append({"name":name , "marks":float(marks)})

average= sum(i["marks"] for i in loadingstudents)/len(loadingstudents)
topper =max(loadingstudents , key=lambda l:l["marks"])
passed =[s["name"] for s in loadingstudents if s["marks"]>=60]


print("\n📄 Student Report")
print("---------------------")
print(f"Class Average: {average:.2f}")
print(f"Topper: {topper['name']} ({topper['marks']:.2f})")
print("Passed Students:", ", ".join(passed))






