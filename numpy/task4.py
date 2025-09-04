import numpy as np
array = np.arange(9)
reshaped=array.reshape(3,3)
flattened=reshaped.flatten()
raveled=reshaped.ravel()
raveled[0]=888
print("orignal:\n", array)
print("\nreshaped: \n", reshaped)
print("\nflattened: ", flattened)
print("\nraveled: ", raveled)