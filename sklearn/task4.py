import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model

"""
⸻

Task: Predict CO2 Emissions Using Linear Regression
	1.	Load the dataset from the given URL into a pandas DataFrame.
	2.	Explore:
	•	Show the first 5 rows.
	•	Show basic statistics (describe()).
	•	Check correlation between ENGINESIZE, CYLINDERS, and CO2EMISSIONS.
	3.	Select features: Use ENGINESIZE and CYLINDERS as your independent variables (X), and CO2EMISSIONS as your dependent variable (y).
	4.	Split the data into training and test sets (80% / 20%).
	5.	Scale the features using StandardScaler.
	6.	Train a LinearRegression model on the training set.
	7.	Print:
	•	Coefficients and intercept (both scaled and converted back to original units).
	•	R² score on training and test data.
	8.	Plot:
	•	Scatter plot of predicted vs actual CO2 emissions for the test set.
	•	Residuals plot (errors vs predicted values)."""

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df=pd.read_csv(url)
print(df.head(5))
print(df.describe())
sdf=df[['ENGINESIZE', 'CYLINDERS',  'CO2EMISSIONS']]
print(sdf.corr())
X=df.iloc[:,[1,2]].to_numpy()
Y=df.iloc[:,[6]].to_numpy()
xtrain,xtest,ytrian,ytest=train_test_split(X,Y,test_size=0.2,random_state=42)
scale=preprocessing.StandardScaler()
std=scale.fit_transform(xtrain)
regressor=linear_model.LinearRegression()
regressor.fit(std,ytrian)
coef_=regressor.coef_
intercept_=regressor.intercept_
mean=scale.mean_
std_dev=np.sqrt(scale.var_)
orinalcoef=coef_/std_dev
oringalintercept=intercept_ - np.sum((mean*coef_)/std_dev)