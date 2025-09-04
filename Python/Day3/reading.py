with open("f2.txt", "r") as file1:
      lines = file1.readlines()

student=[]
for line in lines:  
    name , marks= line.strip().split()
    student.append({"name":name,"marks":int(marks) })


average= sum(s["marks"] for s in student)/len(student)
topper = max(student, key=lambda s: s["marks"])

passed = [s["name"] for s in student if s["marks"]>60]


with open("report.txt", "w") as f:
    f.write(f"Average Marks: {average:.2f}\n")
    f.write(f"Topper: {topper['name']} ({topper['marks']})\n")
    f.write(f"Passed Students: {', '.join(passed)}\n")

print("📄 Report written to report.txt")


