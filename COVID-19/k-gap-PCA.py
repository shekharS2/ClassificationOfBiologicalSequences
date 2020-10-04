#https://towardsdatascience.com/an-approach-to-choosing-the-number-of-components-in-a-principal-component-analysis-pca-3b9f3d6e73fe

#Meaning of StandardScaler().fit_transform()
#The idea behind StandardScaler is that it will transform your data such that its distribution will have a mean value 0 and standard deviation of 1.
#In case of multivariate data, this is done feature-wise (in other words independently for each column of the data).
#Given the distribution of the data, each value in the dataset will have the mean value subtracted, and then divided by the standard deviation of the whole dataset (or feature in the multivariate case)

import pandas as pd

dataset = pd.read_csv("combined-k-gap.csv");

from sklearn.preprocessing import StandardScaler #mean = 0, variance = 1
from sklearn.preprocessing import MinMaxScaler
# Separating out the features
x = dataset.iloc[:, 3:1026].values

# Separating out the target
#y = dataset.iloc[:,['Subtype']].values

# Standardizing the features
scaler = MinMaxScaler(feature_range=[0, 1])
#scaler = StandardScaler()
x = scaler.fit_transform(x)


print('\n\n')
print('==============FEATURES=================')
print(x)

#print('\n\n')
#print('=========================SUBTYPES=============================================')
#print(y)

from sklearn.decomposition import PCA
pca = PCA(n_components=125)
principalComponents = pca.fit_transform(x)

datasetPCA = pd.DataFrame(data = principalComponents, columns = ['principal component1','principal component2','principal component3','principal component4','principal component5','principal component6','principal component7','principal component8','principal component9','principal component10','principal component11','principal component12','principal component13','principal component14','principal component15','principal component16','principal component17','principal component18','principal component19','principal component20','principal component21','principal component22','principal component23','principal component24','principal component25','principal component26','principal component27','principal component28','principal component29','principal component30','principal component31','principal component32','principal component33','principal component34','principal component35','principal component36','principal component37','principal component38','principal component39','principal component40','principal component41','principal component42','principal component43','principal component44','principal component45','principal component46','principal component47','principal component48','principal component49','principal component50','principal component51','principal component52','principal component53','principal component54','principal component55','principal component56','principal component57','principal component58','principal component59','principal component60','principal component61','principal component62','principal component63','principal component64','principal component65','principal component66','principal component67','principal component68','principal component69','principal component70','principal component71','principal component72','principal component73','principal component74','principal component75','principal component76','principal component77','principal component78','principal component79','principal component80','principal component81','principal component82','principal component83','principal component84','principal component85','principal component86','principal component87','principal component88','principal component89','principal component90','principal component91','principal component92','principal component93','principal component94','principal component95','principal component96','principal component97','principal component98','principal component99','principal component100','principal component101','principal component102','principal component103','principal component104','principal component105','principal component106','principal component107','principal component108','principal component109','principal component110','principal component111','principal component112','principal component113','principal component114','principal component115','principal component116','principal component117','principal component118','principal component119','principal component120','principal component121','principal component122','principal component123','principal component124','principal component125'])

finalDataset = pd.concat([datasetPCA, dataset[['Disease','SequenceID', 'Sequence']]], axis = 1)

print('\n\n')
print('===========FINAL DATASET AFTER PCA=============')
print(finalDataset)

finalDataset.to_csv('combined-k-gap-PCA.csv')
#pdFinal = pd.read_csv("k-gap-63-PCA-shuffled.csv")
#print(pdFinal)