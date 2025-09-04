import numpy as np
x = np.array([10, 20, 30])
y = np.array([40, 50, 60])

print("stacking the array\n", np.stack((x,y),axis=-1))
print("vstacking the array\n", np.vstack((x,y)))
print("hstacking the array\n", np.hstack((x,y)))




a = np.arange(1, 13)
parts = np.split(a, 3)
print(parts)
parts1 = np.split(a, 4)
print(parts1)

parts12 = np.array_split(a, 5)  
print(parts12[0])

print(parts12)