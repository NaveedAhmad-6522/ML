student_number=int(input("enter number of students: "))
studentdatabase=[]
for i in range(student_number):
    name , marks , subject =input(f"enter {i+1} student name marks subject respectivly: ").strip().split()
    studentdatabase.append({"name":name,"marks":float(marks),"subject":subject})


with open("studentdatabase.txt","w") as file1:
    for line in studentdatabase:
        file1.write(f"{line['name']},{line['marks']:.2f},{line['subject']} \n")
        
loading=[]
with open("studentdatabase.txt","r") as file2:
    for i in file2:
       name , marks ,subject = i.strip().split(",")
       loading.append({"name":name , "marks":float(marks),"subject":subject })


for i in loading:
    print(f"name: {i['name']} | marks: {i['marks']} | subject: {i['subject']} ")

average =sum([s['marks'] for s in loading])/len(loading)

topper=max(loading,key =lambda s:s['marks'] )
sortedlist=sorted(loading, key =lambda s:s['marks'] , reverse=True)
aboveaverage= [s for s in loading if s['marks']>average]
failed = [s for s in loading if s['marks']<60]
print(f"average: {average}")
print(f"Topper name {topper['name']} marks: {topper['marks']:.2f}")