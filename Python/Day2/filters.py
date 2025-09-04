mylist=[32,32,43,4334]

newlist=list(filter(lambda l:l>100,mylist))
print(newlist)


#task 
tasklist=[12, 98, 35, 66, 100, 48]
task_newlist =list(filter(lambda E:E%2==0,tasklist))
print(task_newlist)


#task of maps and filters combined 

student=[56, 23, 89, 76, 45, 92]

adding5gracemarks=list(map(lambda l:l+5,student))
filtering=list(filter(lambda l:l>60, adding5gracemarks))
