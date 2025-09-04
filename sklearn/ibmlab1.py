import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df=pd.read_csv(url)

print(df.head(5))
print(df.describe())
cdf=df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.hist(color='skyblue')
plt.show()
print(cdf[['ENGINESIZE']])
plt.scatter(cdf['ENGINESIZE'],cdf['CYLINDERS'])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.xlim(0,27)
plt.show()

plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("CYLINDERS")
plt.ylabel("CO2 Emission")
plt.show()

X = cdf['ENGINESIZE'].to_numpy()
Y = cdf.CO2EMISSIONS.to_numpy()

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.2,random_state=42)


#object

regressor = LinearRegression()
regressor.fit(xtrain.reshape(-1,1),ytrain)

print("co-efficinat: ",regressor.coef_[0])
print("intercept : ",regressor.intercept_)

print(ytest,y1test)
 
