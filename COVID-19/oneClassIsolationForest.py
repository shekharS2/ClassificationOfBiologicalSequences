#The implementation is based on an ensemble of ExtraTreeRegressor. The maximum depth of each tree is set to ceil(log_2(n)) where  is the number of samples used to build the tree (see (Liu et al., 2008) for more details).
#https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
#https://towardsdatascience.com/isolation-forest-with-statistical-rules-4dd27dad2da9

#Parameter Tuning: https://machinelearningmastery.com/how-to-tune-algorithm-parameters-with-scikit-learn/


#covid (inlier) = 1
#covid (outlier) = -1

import numpy as np
import pandas as pd
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

from sklearn.ensemble import IsolationForest
clf = IsolationForest(n_estimators=100,
                      max_samples='auto',
                      contamination=0.03, #'auto', 
                      max_features=1.0, 
                      bootstrap=False, 
                      n_jobs=None,
                      behaviour='deprecated',
                      random_state=None, 
                      verbose=0, 
                      warm_start=False).fit(trainData)

prediction = clf.predict(testData)
#print(prediction)

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
plt.title('Coronavirus Detection (Isolation Forest)')
plt.xlabel('Index Nos')
plt.ylabel('Inlier (1 or 2) or Outlier (-1 or -2)')
plt.show()

















