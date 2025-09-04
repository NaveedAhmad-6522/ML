usreinput=int(input("enter number of item: "))
item=[]
for i in range(usreinput):
    name, price =input(f"enter name and marks {i+1} item: ").strip().split()
    item.append({"name":name,"price":float(price)})


with open("item.txt","w") as file1:
    for line in item:
        file1.write(f"{line["name"]} {line["price"]:.2f} \n")


reading =[]

with open("item.txt", "r") as file2:
    for line in file2:
        name , price =line.strip().split()
        reading.append({"name":name, "price":price})



#printinf left allign
for i in reading:
    print(f"{i['name']}  {i['price']}")



#bill

totalbiil= (sum(float(i['price']) for i in reading))
print(totalbiil)