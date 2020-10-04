#https://towardsdatascience.com/anomaly-detection-with-pyod-b523fc47db9
#https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/
#https://pypi.org/project/pyod/

#Outlier Detection

#in scikit-learn '-1' means outlier and '1' means inlier
#in pyod '1' means outlier and '0' means inlier

import pandas as pd
import numpy as np
#import matplotlib.pyplot as mlt

datasetCorona = pd.read_csv("corona-k-gap-5000.csv")
datasetCombined = pd.read_csv("combined-k-gap-unseen-5000.csv")

trainData = datasetCorona.iloc[:5000, 3:1026].values
#print(trainData)
#no train target as one-class classification
trainTarget = datasetCorona.iloc[:5000, 0].values

testData = datasetCombined.iloc[:1000, 4:1027].values
#print(testData)
testTarget = datasetCombined.iloc[:1000, 0].values
print(testTarget)
for i in range(len(testTarget)):
    if testTarget[i] == -1:
        testTarget[i] = 1
    elif testTarget[i] == 1:
        testTarget[i] = 0
print(testTarget)




from pyod.models.knn import KNN   # kNN detector

#contamination = 0.1  # percentage of outliers
#n_train = 200  # number of training points
#n_test = 100  # number of testing points

#X_train, y_train, X_test, y_test = generate_data(n_train=n_train, n_test=n_test, contamination=contamination)

# train kNN detector
clf_name = 'KNN'
clf = KNN(contamination=0.5,
          n_neighbors=5,
          method='largest',
          radius=1.0,
          algorithm='auto',
          leaf_size=30,
          metric='minkowski',
          p=2,
          metric_params=None,
          n_jobs=1)

clf.fit(trainData)

# get the prediction labels and outlier scores of the training data
y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
#print(y_train_pred)
y_train_scores = clf.decision_scores_  # raw outlier scores
#print(y_train_scores)

# get the prediction on the test data
y_test_pred = clf.predict(testData)#X_test)  # outlier labels (0 or 1)
print(y_test_pred)

from sklearn.metrics import accuracy_score
accuracy_percentage = accuracy_score(testTarget, y_test_pred) * 100
print("The prediction accuracy is:", end = " ")
print(accuracy_percentage)



y_test_scores = clf.decision_function(testData)#X_test)  # outlier scores
#print(y_test_scores)






# evaluate and print the results
#print("\nOn Training Data:")
#evaluate_print(clf_name, y_train, y_train_scores)
#print("\nOn Test Data:")
#evaluate_print(clf_name, y_test, y_test_scores)

#isualize(clf_name, trainData, trainTarget, testData, testTarget, y_train_pred,
#          y_test_pred, show_figure=True, save_figure=False)






















