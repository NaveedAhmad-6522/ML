
user_input=input("Ente Your Name:" )
marks=float(input("Ente Your Marks:" ))
print(f"Hello, {user_input}")

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
