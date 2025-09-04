import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.tree import DecisionTreeClassifier ,plot_tree
path= 'drug200.csv'
df=pd.read_csv(path)
print(df['BP'].head())
LabelEncoder=LabelEncoder()
df['Sex']=LabelEncoder.fit_transform(df['Sex'])
df['BP']=LabelEncoder.fit_transform(df['BP'])
df['Cholesterol']=LabelEncoder.fit_transform(df['Cholesterol'])
print(df['BP'].head())
custommap = {'DrugA': 0, 'DrugB': 1, 'DrugC': 2, 'DrugX': 3, 'DrugY': 4}
df['Drug'] = df['Drug'].str.strip().str.title()
df['Drug_num'] = df['Drug'].map(custommap)
correlation=df.drop('Drug',axis=1).corr()['Drug_num']
print(correlation)
import seaborn as sns
import matplotlib.pyplot as plt
category_counts = df['Drug'].value_counts()
# Plot the count plot
plt.bar(category_counts.index, category_counts.values, color='blue')
plt.xlabel('Drug')
plt.ylabel('Count')
plt.title('Category Distribution')
plt.xticks(rotation=45)  # Rotate labels for better readability if needed

X=df.drop(['Drug','Drug_num'],axis=1)
y=df['Drug']
print(X,"\n",y)
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
dTree=DecisionTreeClassifier(criterion="entropy", max_depth = 4)
dTree.fit(xtrain,ytrain)
ypred=dTree.predict(xtest)
from sklearn import metrics
print("Accuracy",metrics.accuracy_score(ytest,ypred)*100)

plot_tree(dTree)
plt.show()

dTree=DecisionTreeClassifier(criterion="entropy", max_depth = 3)
dTree.fit(xtrain,ytrain)
ypred=dTree.predict(xtest)
print("Accuracy",metrics.accuracy_score(ytest,ypred)*100)

plot_tree(dTree)
plt.show()
#df['Drug']=LabelEncoder.fit_transform(df['Drug'])
"""
df['Drug']=df['Drug'].astype('category').cat.codes
#print(df['Drug'].unique())
custommap = {'DrugA': 0, 'DrugB': 1, 'DrugC': 2, 'DrugX': 3, 'DrugY': 4}
df['Drug'] = df['Drug'].str.strip().str.title()
df['Drug'] = df['Drug'].map(custommap)
"""