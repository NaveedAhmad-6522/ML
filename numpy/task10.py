import numpy as np

a = np.array([[10, 20, 30],
             [10, 20, 30]])
print(a.shape)  # (3,)

b = np.expand_dims(a, axis=0)  # Add a row dimension → shape (1, 3)
c = np.expand_dims(a, axis=1)  # Add a column dimension → shape (3, 1)

print("Row vector:\n", b, b.shape)
print("Column vector:\n", c, c.shape)