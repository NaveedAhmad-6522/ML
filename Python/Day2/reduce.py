from functools import reduce
marks = [56, 89, 90, 75, 60]
sum_of_marks=reduce(lambda x,y :x+y,marks)
average =sum_of_marks/len(marks)
print(sum_of_marks)
print(average)



maxnum=reduce(lambda x,y:x if x>y else y, marks)
