import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans 
data = pd.read_csv('3.01 Country.csv')
data 
# country latitude longitude language
plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-180, 180)
plt.ylim(-90, 90)
x=data.iloc[:,1:3]
kmeans=KMeans(2)
kmeans.fit(x)
identified_clusters = kmeans.fit_predict(x)
identified_clusters

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters

data_mapped = data.copy()
data_mapped['Language']=data_mapped['Language'].map({'English':0,'French':1})
data_mapped
x=data_mapped[:,3:4]

kmeans.inertia_

#Market Segmentation
data

# Satisfaction Loyalty
plt.scatter(data['Satisfcation'], data['Loyalty'])
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
x=data.copy()
kmeans=KMeans(2)
kmeans.fit(x)

from sklearn import preprocessing
x_scaled  = preprocessing.scale(x)
x_scaled

# Heatmap and Dendograms
data = pd.read_csv('Country clusters.csv', index_col='Country')
x_scaled=data.copy()
x_scaled=x_scaled.drop(['Language'], axis=1)
sns.clustermap(x_scaled)


