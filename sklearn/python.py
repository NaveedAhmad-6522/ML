import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[1.0], [2.0], [3.0]])
scaler = StandardScaler()

X_std = scaler.fit_transform(X)
print(X_std)