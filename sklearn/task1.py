import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create simple dataset
data = {
    'HouseSize (sqft)': [1000, 1500, 2000, 2500, 3000],
    'Price ($)': [100000, 150000, 200000, 250000, 300000]
}

df = pd.DataFrame(data)

# Step 2: Split data into X (input) and y (output)
X = df[['HouseSize (sqft)']]  # Features must be 2D
y = df['Price ($)']           # Target

# Step 3: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict
y_pred = model.predict(X)

# Step 5: Visualize
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, y_pred, color='red', label='Predicted Line')
plt.xlabel('House Size (sqft)')
plt.ylabel('Price ($)')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

# Step 6: Evaluate
print("Mean Squared Error:", mean_squared_error(y, y_pred))
print("R² Score:", r2_score(y, y_pred))
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)