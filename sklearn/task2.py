import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = [850, 1100, 1500, 1800, 2100, 5000]
y = [45, 55, 72, 85, 95, 110]

# Convert to NumPy array
X = np.array(X)
y = np.array(y)

# Reshape X for sklearn
X_reshaped = X.reshape(-1, 1)

# Create and train model
regressor = LinearRegression()
regressor.fit(X_reshaped, y)

# Predictions
pred_1600 = regressor.predict([[1600]])[0]
pred_2300 = regressor.predict([[2300]])[0]
print(f"PRE {pred_1600}")
#print(f"Predicted price for 1600 sqft: {pred_1600:.2f} Lakh PKR")
print(f"Predicted price for 2300 sqft: {pred_2300:.2f} Lakh PKR")

# Plot data points
plt.scatter(X, y, color='blue', label='Data')

# Plot regression line
plt.plot(X, regressor.predict(X_reshaped), color='red', label='Regression Line')

# Plot predicted points
plt.scatter([1600, 2300], [pred_1600, pred_2300], color='green', label='Predictions')

# Add labels and title
plt.xlabel("Area (sqft)")
plt.ylabel("Price (Lakh PKR)")
plt.title("House Price Prediction")
plt.legend()
plt.grid(True)
plt.show()