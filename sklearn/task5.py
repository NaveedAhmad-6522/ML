import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
from sklearn.preprocessing import StandardScaler ,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
filePath="data.csv"
df=pd.read_csv(filePath)
sns.countplot(y='NObeyesdad',data=df)
continous_columns=df.select_dtypes(include=['Float64']).columns.tolist()
scaler=StandardScaler()
scaler_fearure=scaler.fit_transform(df[continous_columns])
scaler_df=pd.DataFrame(scaler_fearure,columns=scaler.get_feature_names_out(continous_columns))
scaled_data=pd.concat([df.drop(continous_columns,axis=1),scaler_df],axis=1)
catagories_columns = scaled_data.select_dtypes(include=['object']).columns.tolist()
if 'NObeyesdad' in catagories_columns:
    catagories_columns.remove('NObeyesdad')
encoder=OneHotEncoder(sparse_output=False,drop='first')
encoded=encoder.fit_transform(scaled_data[catagories_columns])
catagories_columnsDF=pd.DataFrame(encoded,columns=encoder.get_feature_names_out(catagories_columns))
preped_data=pd.concat([scaled_data.drop(catagories_columns,axis=1),catagories_columnsDF],axis=1)
preped_data['NObeyesdad'] = df['NObeyesdad'].astype('category').cat.codes
X=preped_data.drop('NObeyesdad',axis=1)
y=preped_data['NObeyesdad']
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=4,stratify=y)
regressor=LogisticRegression(multi_class='ovr',max_iter=1000)
regressor.fit(xtrain,ytrain)
ypred=regressor.predict(xtest)
print(np.round(accuracy_score(ytest,ypred)*100,2))
# Plot for One-vs-Rest predictions
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.scatter(ypred, ytest, label="Actual", alpha=0.7)
plt.scatter(range(len(ypred)), ypred, label="Predicted (OvR)", alpha=0.7)
plt.title("Actual vs Predicted (OvR)")
plt.xlabel("Sample Index")
plt.ylabel("Class")
plt.legend()

model_ovo=OneVsOneClassifier(LogisticRegression())
regressor_ovo=model_ovo.fit(xtrain,ytrain)
predovo=regressor_ovo.predict(xtest)
print(np.round(accuracy_score(ytest,predovo)*100,2))




# Plot for One-vs-One predictions
plt.subplot(1,2,2)
plt.scatter(range(len(ytest)), ytest, label="Actual", alpha=0.7)
plt.scatter(range(len(ypred)), predovo, label="Predicted (OvO)", alpha=0.7)
plt.title("Actual vs Predicted (OvO)")
plt.xlabel("Sample Index")
plt.ylabel("Class")
plt.legend()

plt.tight_layout()
plt.show()