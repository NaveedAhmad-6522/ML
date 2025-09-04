import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("teleCust1000t.csv")
df.head()
df.custcat.value_counts()
correlation_matrix=df.corr()
print(correlation_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()
correlation_values=np.abs(df.corr().custcat.drop('custcat').sort_values(ascending=False))
print(correlation_values)

X=df.drop(columns=['custcat'])
y=df.custcat
X_norm=StandardScaler().fit_transform(X)

X_train,X_test,y_train,y_test=train_test_split(X_norm,y,test_size=0.2,random_state=4,stratify=y)
k=6
knn_classifier=KNeighborsClassifier(n_neighbors=k)
knn_model=knn_classifier.fit(X_train,y_train)
 
yhat=knn_model.predict(X_test)
print("Test set Accuracy: ", accuracy_score(y_test, yhat))

Ks=100
acc=np.zeros((Ks))
std_acc=np.zeros((Ks))

for i in range(1,Ks+1):
    knn_model_n=KNeighborsClassifier(n_neighbors=i).fit(X_train,y_train)
    yhat=knn_model_n.predict(X_test)
    acc[i-1]=accuracy_score(y_test,yhat)
    std_acc[i-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])/np.sqrt(yhat.shape[0])

print( "The best accuracy was with", acc.max(), "with k =", acc.argmax()+1) 
plt.plot(range(1,Ks+1),acc,'g')
plt.fill_between(range(1,Ks+1),acc-1*std_acc,acc+1*std_acc,alpha=0.30)
plt.legend(('Accuracy value', 'Standard Deviation'))
plt.ylabel('Model Accuracy')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()