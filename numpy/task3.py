

import numpy as np

# Step 1: Create a 4x4 matrix
a = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120],
              [130, 140, 150, 160]])

# Step 2: Create a 1D array with 4 values
b = np.array([1, 2, 3, 4])

# Step 3: Broadcast b to each row of a
broadcast_result = a + b
print("Broadcasted Result:\n", broadcast_result)

# Step 4: Subtract column-wise mean from each column
col_mean = np.mean(broadcast_result, axis=0)
normalized = broadcast_result - col_mean
print("\nColumn-wise mean:\n", col_mean)

print("\nNormalized Result:\n", normalized)

# Step 5: Calculate and display row-wise and column-wise sums
row_sum = np.sum(broadcast_result, axis=1)
col_sum = broadcast_result.sum( axis=0)
print("\nRow-wise Sum:\n", row_sum)
print("\nColumn-wise Sum:\n", col_sum)
