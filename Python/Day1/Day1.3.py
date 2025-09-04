'''Practice Tasks for You (🔥 Try Now):

Task 1: Basic List Practice
	1.	Create a list of 5 student names.
	2.	Print the first and last student.
	3.	Add a new student.
	4.	Sort the list and print it.

Task 2: List of Marks
	1.	Ask the user to enter marks of 5 students (use a loop + append()).
	2.	After input, print:
	•	The highest mark
	•	The average
	•	How many students scored above 60

Let me know when you’re done or if you want help building it step by step 🧠
You’re doing amazing, Naveed. Let’s keep leveling up 🐍💪 

my_list= ["naveed","basit","omar","jamal","haris"]
print(my_list[4],my_list[0])

my_list.append("sahib g")
my_list.sort()

print("sorted list", my_list)'''

my1_list =[]
for i in range(5):
    marks=float(input("enter marks"))
    my1_list.append(marks)
highest =max(my1_list)
totalsum=sum(my1_list)
average = totalsum / len(my1_list)
print(highest, average)

studentsabove65=0
for i in my1_list:
    if i>64:
        studentsabove65 += 1
print("above 64 \n", studentsabove65)