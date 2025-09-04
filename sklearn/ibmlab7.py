import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler,normalize
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
from sklearn.utils.class_weight import compute_sample_weight

url= "creditcard.csv"

# read the input data
raw_data=pd.read_csv(url)
labels=raw_data.Class.unique()
size=raw_data.Class.value_counts().values
print(size)
fig,ax=plt.subplots()
ax.pie(size,labels=labels,autopct='%1.3f%%')
ax.set_title('Target Variable Value Counts')
correlation=raw_data.corr()['Class'].drop('Class')

correlation.plot(kind='barh', figsize=(10, 6))
print(correlation)
raw_data.iloc[:,1:30]=StandardScaler().fit_transform(raw_data.iloc[:,1:30])
data_matrix=raw_data.values
X=raw_data.iloc[:,1:30]
y=raw_data.iloc[:,30]
print(type(X))
X = normalize(X, norm="l1")
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=43)
w_train = compute_sample_weight('balanced', y_train)
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=4, random_state=35)
dt.fit(X_train, y_train, sample_weight=w_train)

svm = LinearSVC(class_weight='balanced', random_state=31, loss="hinge", fit_intercept=False)

svm.fit(X_train, y_train)
y_pred_dt = dt.predict_proba(X_test)[:,1]
from sklearn.metrics import roc_auc_score
roc_auc_dt = roc_auc_score(y_test, y_pred_dt)
print('Decision Tree ROC-AUC score : {0:.3f}'.format(roc_auc_dt))

y_pred_svm = svm.decision_function(X_test)

roc_auc_svm = roc_auc_score(y_test, y_pred_svm)
print("SVM ROC-AUC score: {0:.3f}".format(roc_auc_svm))

'''# your code goes here
correlation_values = abs(raw_data.corr()['Class']).drop('Class')
correlation_values = correlation_values.sort_values(ascending=False)[...]
correlation_values

# Replace the statement defining the variable `X` with the following and run the cell again.
X = data_matrix[:,[3,10,12,14,16,17]]'''