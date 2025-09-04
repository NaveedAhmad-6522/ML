
mylist=[34,32,75]
def add10toeach(i):
     return i+10

new_list=list( map(add10toeach,mylist))
print(new_list)
listwithlambda=list(map(lambda s:s+10,mylist))
print(listwithlambda)


tasklist=[45, 76, 29, 90, 55]
tasklist=list(map(lambda s:s*100/50,tasklist))
print(tasklist)
