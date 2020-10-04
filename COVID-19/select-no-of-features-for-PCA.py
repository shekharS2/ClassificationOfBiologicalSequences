#https://towardsdatascience.com/an-approach-to-choosing-the-number-of-components-in-a-principal-component-analysis-pca-3b9f3d6e73fe
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

filepath = 'corona-k-gap.csv' #your path here
data = np.genfromtxt(filepath, delimiter=',', dtype='float64') #row for feature names is included

scaler = MinMaxScaler(feature_range=[0, 1])
#scaler = StandardScaler()
data_rescaled = scaler.fit_transform(data[1:, 3:1026])
#print(len(data))

#Fitting the PCA algorithm with our Data
pca = PCA().fit(data_rescaled)  
#Plotting the Cumulative Summation of the Explained Variance
plt.grid(True, linewidth=0.5, color='#ff0000', linestyle='-')
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Variance (%)') #for each component
plt.title('Dataset Explained Variance')
plt.show()
