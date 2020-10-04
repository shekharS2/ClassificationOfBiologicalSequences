import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datasetCorona = pd.read_csv("corona-k-gap-5000.csv")
datasetCombined = pd.read_csv("combined-k-gap-unseen-5000.csv")

trainData = datasetCorona.iloc[:5000, 3:1026].values
#print(trainData)
#no train target as one-class classification

testData = datasetCombined.iloc[:1000, 4:1027].values
#print(testData)
testTarget = datasetCombined.iloc[:1000, 0].values
#print(testTarget)

from sklearn.svm import OneClassSVM
clf = OneClassSVM(kernel="rbf", nu = 0.1, degree = 3, gamma = 50).fit(trainData)
prediction = clf.predict(testData)
print(prediction)

from sklearn.metrics import accuracy_score
accuracy_percentage = accuracy_score(testTarget, prediction) * 100
print("The prediction accuracy is:", end = " ")
print(accuracy_percentage)

###################################################################################
#Plotting
index = np.arange(1,1001,1)
index = index.reshape(index.shape[0],1)

testTarget = np.array(testTarget)
testTarget = testTarget.reshape(testTarget.shape[0],1)

prediction = np.array(prediction)
prediction[prediction>0] = 2
prediction[prediction<0] = -2
prediction = prediction.reshape(prediction.shape[0],1)



plt.scatter(index, testTarget, color = 'red')
plt.scatter(index, prediction, color = 'blue')
plt.title('Coronavirus Detection (SVM)')
plt.xlabel('Index Nos')
plt.ylabel('Inlier (1 or 2) or Outlier (-1 or -2)')
plt.show()

