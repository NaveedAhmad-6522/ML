mylist=["naveed","basit","asad","zarar","jawad"]
with open("f1.txt","w")as f:
  for name in mylist:
   f.write(name + "\n")
