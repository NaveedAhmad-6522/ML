
import numpy as np

a = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120],
              [130, 140, 150, 160]])


for i in a:
    for item in i:
     if(item>100):
        print(f"{item} \n")



print(a[a>100])







a[a<50]=0

print(a)