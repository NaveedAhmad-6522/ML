
names =[]


for i in range(5):
    name =input(f"enter name  {i+1} : ")
    names.append(name)


with open("names.txt" , "w") as file1:
     file1.write(",".join(names))
     
