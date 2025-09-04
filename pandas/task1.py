'''datafom and series'''

import pandas as pd
#Create a Series showing 4 subjects and their marks.
subjects=["physic","maths","DSA","DSD"]
marks=[56,23,56,23]
Series=pd.Series(data=marks,index=subjects)
print(Series)

#Create a DataFrame of students with columns: Name, CGPA, Degree.


Name=["Naveed","Basit","Zarar"]
CGPA=[3.3,3.6,3.9]
Degree=["BS","BSc","PhD"]
dataforn=pd.DataFrame({
 "Name"  :Name,
 "Degree":Degree,
 "CGPA"  :CGPA

})
print(dataforn)
