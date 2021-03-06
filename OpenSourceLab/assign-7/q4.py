# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = pd.read_csv("OpenSourceLab/assign-7/iris.csv")

X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
#Split arrays or matrices into train and test subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
a_index = list(range(1, 11))
a = pd.Series()
# Calculate the accuracy of the model for different values of k
for i in np.arange(1, 10):
    knn2 = KNeighborsClassifier(n_neighbors=i)
    knn2.fit(X_train, y_train)
    print("For k = %d accuracy is" % i, knn2.score(X_test, y_test))
# Visual presentation: Various values of n for K-Nearest nerighbours
print("\nVisual presentation: Various values of n for K-Nearest nerighbours:")
for i in list(range(1, 11)):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    a = a.append(pd.Series(metrics.accuracy_score(prediction, y_test)))
plt.plot(a_index, a)
plt.show()

"""
For k = 1 accuracy is 0.9666666666666667
For k = 2 accuracy is 0.9666666666666667
For k = 3 accuracy is 0.9666666666666667
For k = 4 accuracy is 0.9666666666666667
For k = 5 accuracy is 0.9666666666666667
For k = 6 accuracy is 0.9666666666666667
For k = 7 accuracy is 0.9666666666666667
For k = 8 accuracy is 0.9666666666666667
For k = 9 accuracy is 0.9666666666666667

Visual presentation: Various values of n for K-Nearest nerighbours:
PS D:\Work\JIIT\Sem__5\Sem_5>

 """
