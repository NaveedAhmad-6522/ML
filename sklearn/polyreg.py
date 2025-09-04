import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Create the dataset
data = {
    'Size': [500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750],
    'Price': [150, 200, 250, 300, 370, 430, 480, 520, 580, 600]
}
df = pd.DataFrame(data)

# Step 2: Prepare feature matrix X and target vector y
X = df[['Size']].values   # 2D array required for sklearn
y = df['Price'].values    # 1D array target

# Step 3: Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create polynomial features (degree=2 for quadratic curve)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Step 5: Train Linear Regression model on polynomial features
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Step 6: Make predictions on test set
y_pred = model.predict(X_test_poly)

# Step 7: Print coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Step 8: Plot results
plt.scatter(X, y, color='blue', label='Original data')
# For smooth curve plot, generate a range of sizes
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
X_range_poly = poly.transform(X_range)
y_range_pred = model.predict(X_range_poly)
plt.plot(X_range, y_range_pred, color='red', label='Polynomial fit')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price (thousands $)')
plt.title('Polynomial Regression: House Price vs Size')
plt.legend()
plt.show()