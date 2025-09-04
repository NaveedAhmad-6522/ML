import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import linear_model
url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

df=pd.read_csv(url)
df = df.drop(['MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE',],axis=1)
print(df.corr())
df = df.drop(['CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB',],axis=1)
print(df.head(9))
axes=pd.plotting.scatter_matrix(df,alpha=0.2)
for ax in axes.flatten():
    ax.xaxis.label.set_rotation(90)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')


plt.gcf().subplots_adjust(wspace=0,hspace=0)
plt.tight_layout()
plt.show()
X=df.iloc[:,[0,1]].to_numpy()
y=df.iloc[:,[2]].to_numpy()

#preprocessing

std_scaler=preprocessing.StandardScaler()
X_std=std_scaler.fit_transform(X)

pd.DataFrame(X_std).round(2)

X_train,X_test,y_train,y_test=train_test_split(X_std,y,test_size=0.2,random_state=42)

regeressor=linear_model.LinearRegression()
regeressor.fit(X_train,y_train)

coef_=regeressor.coef_
intercept_=regeressor.intercept_

#original coefficint and intercept_

mean_=std_scaler.mean_
var_=std_scaler.var_
std_dev=np.sqrt(var_)
coef_original=coef_/std_dev
original_intercept=intercept_ - np.sum((mean_ * coef_)/std_dev)

X1=X_test[:,0] if X_test.ndim>1 else X_test
X2=X_test[:,1] if X_test.ndim>1 else np.zeros_like(X1)

x1_surf, x2_surf = np.meshgrid(np.linspace(X1.min(), X1.max(), 100), 
                               np.linspace(X2.min(), X2.max(), 100))
y_surf=intercept_ + coef_[0,0]*x1_surf +coef_[0,1]*x2_surf

y_pred = regeressor.predict(X_test.reshape(-1, 1)) if X_test.ndim == 1 else regeressor.predict(X_test)
above_plane = y_test >= y_pred
below_plane = y_test < y_pred
above_plane = above_plane[:,0]
below_plane = below_plane[:,0]

# Plotting
fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data points above and below the plane in different colors
ax.scatter(X1[above_plane], X2[above_plane], y_test[above_plane], color='red', label="Above Plane",s=70,alpha=.7,ec='k')
ax.scatter(X1[below_plane], X2[below_plane], y_test[below_plane],  color='blue', label="Below Plane",s=50,alpha=.3,ec='k')

ax.plot_wireframe(x1_surf, x2_surf, y_surf, color='k', linewidth=0.5)
ax.plot_surface(x1_surf, x2_surf, y_surf, color='k', alpha=0.21,label='plane',linewidth=0.5)

# Set view and labels
ax.view_init(elev=10)

ax.legend(fontsize='x-large',loc='upper center')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect(None, zoom=0.75)
ax.set_xlabel('ENGINESIZE', fontsize='xx-large')
ax.set_ylabel('FUELCONSUMPTION', fontsize='xx-large')
ax.set_zlabel('CO2 Emissions', fontsize='xx-large')
ax.set_title('Multiple Linear Regression of CO2 Emissions', fontsize='xx-large')
plt.tight_layout()
plt.show()