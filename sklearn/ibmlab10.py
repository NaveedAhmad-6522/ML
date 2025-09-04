import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
from sklearn.datasets import make_blobs 
from sklearn.preprocessing import StandardScaler
import plotly.express as px



import warnings
warnings.filterwarnings('ignore')
np.random.seed(0)
X,y=make_blobs(n_samples=5000,centers=[[4,4],[-2,-1],[2,-2],[1,1]],cluster_std=0.9)
plt.scatter(X[:,0],X[:,1],marker='.',alpha=0.3,ec='k',s=80)


k_means = KMeans(init = "k-means++", n_clusters = 4, n_init = 12)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
fig=plt.figure(figsize=(6,4))
colors=plt.cm.tab10(np.linspace(0,1,len(set(k_means_labels))))
ax=fig.add_subplot(1,1,1)
zipping=zip(range(len([[4,4],[-2,-1],[2,-2],[1,1]])),colors)

for k,col in zipping:
    my_members=(k_means_labels==k)
    cluster_center=k_means_cluster_centers[k]
    ax.plot(X[my_members,0],X[my_members,1],'w',markerfacecolor=col,marker='.',ms=10)
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)
ax.set_title('KMeans')

# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot
k_means3 = KMeans(init="k-means++", n_clusters=3, n_init=12)
k_means3.fit(X)
fig = plt.figure(figsize=(6, 4))
colors = plt.cm.tab10(np.linspace(0, 1, len(set(k_means3.labels_))))
ax = fig.add_subplot(1, 1, 1)
for k, col in zip(range(len(k_means3.cluster_centers_)), colors):
    my_members = (k_means3.labels_ == k)
    cluster_center = k_means3.cluster_centers_[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w', markerfacecolor=col, marker='.',ms=10)
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,  markeredgecolor='k', markersize=6)


k_means5=KMeans(init='k-means++',n_clusters=5,n_init=12)
k_means5.fit(X)
k_means5_labels=k_means5.labels_
k_means5_centers=k_means5.cluster_centers_

fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot(1,1,1)
colors=plt.cm.tab10(np.linspace(0,1,len(set(k_means5_labels))))
print(colors)
for k,color in zip(range(len(k_means5_centers)),colors):
    my_members5=(k_means5_labels==k)
    cluster_center5=k_means5_centers[k]
    ax.plot(X[my_members5,0],X[my_members5,1],'w',marker='.',markerfacecolor=color,ms=10)
    ax.plot(cluster_center5[0],cluster_center5[1],'o',marker='.',markeredgecolor='k',markerfacecolor=color,ms=6)
ax.set_title('KMeans')

# Remove x-axis ticks
ax.set_xticks(())

# Remove y-axis ticks
ax.set_yticks(())

# Show the plot

cust_df = pd.read_csv("clustering.csv")
cust_df=cust_df.drop("Address",axis=1)
cust_df=cust_df.dropna()
print(cust_df.info())
X=cust_df.values[:,1:]
Clus_dataSet=StandardScaler().fit_transform(X)
k=3
Kmean=KMeans(init='k-means++',n_clusters=k,n_init=12)
Kmean.fit(Clus_dataSet)

labels_=Kmean.labels_
centers_=Kmean.cluster_centers_
cust_df["Clus_km"] = labels_
print(cust_df['Clus_km'].unique())


area = np.pi * ( X[:, 1])**2  
plt.scatter(X[:, 0], X[:, 3], s=area, c=labels_.astype(float), cmap='tab10', ec='k',alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)
plt.show()

fig = px.scatter_3d(X, x=1, y=0, z=3, opacity=0.7, color=labels_.astype(float))

fig.update_traces(marker=dict(size=5, line=dict(width=.25)), showlegend=False)
fig.update_layout(coloraxis_showscale=False, width=1000, height=800, scene=dict(
        xaxis=dict(title='Education'),
        yaxis=dict(title='Age'),
        zaxis=dict(title='Income')
    ))  # Remove color bar, resize plot

fig.show()