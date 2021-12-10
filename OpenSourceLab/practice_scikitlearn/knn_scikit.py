import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.tools.datetimes import Scalar

names = ["sepal_length", "sepal_width"," petal_length"," petal_width"," species"]

dataset = pd.read_csv("OpenSourceLab/practice_scikitlearn/iris.csv",names=names)

print(dataset.head())

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20)


from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()

scalar.fit(x_train)

x_train=scalar.transform(x_train)
x_test=scalar.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier

clasifier=KNeighborsClassifier(n_neighbors=5)
clasifier.fit(x_train,y_train)

y_pred =clasifier.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

