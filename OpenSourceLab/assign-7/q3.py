import pandas as pd
from sklearn.model_selection import train_test_split
iris = pd.read_csv("OpenSourceLab/assign-7/iris.csv")

X = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values
#Split arrays or matrices into random train and test subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
print("\n70% train data:")
print(X_train)
print(y_train)
print("\n30% test data:")
print(X_test)
print(y_test)

"""

70% train data:
[[5.5 2.4 3.7 1. ]
 [6.8 3.  5.5 2.1]
 [6.1 3.  4.6 1.4]
 [6.  2.2 5.  1.5]
 [6.3 3.3 4.7 1.6]
 [5.9 3.  5.1 1.8]
 [6.1 2.9 4.7 1.4]
 [6.9 3.1 5.4 2.1]
 [5.4 3.9 1.3 0.4]
 [5.7 2.9 4.2 1.3]
 [5.7 3.  4.2 1.2]
 [6.3 2.5 5.  1.9]
 [5.  3.6 1.4 0.2]
 [6.4 3.2 4.5 1.5]
 [5.1 2.5 3.  1.1]
 [6.4 2.8 5.6 2.1]
 [4.8 3.1 1.6 0.2]
 [6.7 3.3 5.7 2.5]
 [7.6 3.  6.6 2.1]
 [5.5 2.4 3.8 1.1]
 [5.1 3.8 1.9 0.4]
 [4.8 3.  1.4 0.3]
 [4.4 2.9 1.4 0.2]
 [6.9 3.2 5.7 2.3]
 [4.6 3.6 1.  0.2]
 [5.6 2.8 4.9 2. ]
 [6.1 2.6 5.6 1.4]
 [6.4 2.9 4.3 1.3]
 [4.4 3.2 1.3 0.2]
 [5.2 2.7 3.9 1.4]
 [6.6 2.9 4.6 1.3]
 [6.3 2.8 5.1 1.5]
 [5.1 3.8 1.5 0.3]
 [6.1 2.8 4.  1.3]
 [6.2 2.9 4.3 1.3]
 [6.2 3.4 5.4 2.3]
 [5.1 3.3 1.7 0.5]
 [4.8 3.  1.4 0.1]
 [4.9 3.1 1.5 0.1]
 [5.  3.4 1.5 0.2]
 [7.7 3.8 6.7 2.2]
 [5.  2.  3.5 1. ]
 [7.7 2.6 6.9 2.3]
 [4.6 3.2 1.4 0.2]
 [7.7 2.8 6.7 2. ]
 [6.3 2.5 4.9 1.5]
 [5.  3.2 1.2 0.2]
 [4.9 3.  1.4 0.2]
 [4.4 3.  1.3 0.2]
 [7.2 3.2 6.  1.8]
 [4.9 2.5 4.5 1.7]
 [6.5 3.  5.8 2.2]
 [4.8 3.4 1.9 0.2]
 [7.4 2.8 6.1 1.9]
 [6.1 3.  4.9 1.8]
 [6.5 3.  5.5 1.8]
 [5.6 2.7 4.2 1.3]
 [6.7 3.  5.2 2.3]
 [5.7 2.8 4.5 1.3]
 [5.8 2.7 3.9 1.2]
 [6.3 3.4 5.6 2.4]
 [7.1 3.  5.9 2.1]
 [6.7 2.5 5.8 1.8]
 [6.8 3.2 5.9 2.3]
 [6.4 2.8 5.6 2.2]
 [4.6 3.1 1.5 0.2]
 [5.6 2.5 3.9 1.1]
 [5.8 2.6 4.  1.2]
 [5.6 2.9 3.6 1.3]
 [6.7 3.3 5.7 2.1]
 [5.2 3.4 1.4 0.2]
 [5.1 3.7 1.5 0.4]
 [5.5 2.5 4.  1.3]
 [6.  2.7 5.1 1.6]
 [4.5 2.3 1.3 0.3]
 [4.3 3.  1.1 0.1]
 [6.  3.  4.8 1.8]
 [5.4 3.9 1.7 0.4]
 [5.1 3.5 1.4 0.3]
 [5.7 3.8 1.7 0.3]
 [7.7 3.  6.1 2.3]
 [6.5 3.2 5.1 2. ]
 [4.6 3.4 1.4 0.3]
 [6.  2.9 4.5 1.5]
 [5.1 3.4 1.5 0.2]
 [5.8 2.7 4.1 1. ]
 [4.7 3.2 1.3 0.2]
 [5.1 3.8 1.6 0.2]
 [6.8 2.8 4.8 1.4]
 [6.9 3.1 5.1 2.3]
 [5.5 2.6 4.4 1.2]
 [5.5 4.2 1.4 0.2]
 [5.  3.5 1.6 0.6]
 [5.6 3.  4.1 1.3]
 [5.1 3.5 1.4 0.2]
 [5.4 3.  4.5 1.5]
 [5.8 4.  1.2 0.2]
 [6.7 3.  5.  1.7]
 [6.1 2.8 4.7 1.2]
 [6.5 3.  5.2 2. ]
 [5.  3.3 1.4 0.2]
 [7.3 2.9 6.3 1.8]
 [6.9 3.1 4.9 1.5]
 [5.4 3.4 1.5 0.4]
 [5.8 2.8 5.1 2.4]]
[1.  2.1 1.4 1.5 1.6 1.8 1.4 2.1 0.4 1.3 1.2 1.9 0.2 1.5 1.1 2.1 0.2 2.5
 2.1 1.1 0.4 0.3 0.2 2.3 0.2 2.  1.4 1.3 0.2 1.4 1.3 1.5 0.3 1.3 1.3 2.3
 0.5 0.1 0.1 0.2 2.2 1.  2.3 0.2 2.  1.5 0.2 0.2 0.2 1.8 1.7 2.2 0.2 1.9
 1.8 1.8 1.3 2.3 1.3 1.2 2.4 2.1 1.8 2.3 2.2 0.2 1.1 1.2 1.3 2.1 0.2 0.4
 1.3 1.6 0.3 0.1 1.8 0.4 0.3 0.3 2.3 2.  0.3 1.5 0.2 1.  0.2 0.2 1.4 2.3
 1.2 0.2 0.6 1.3 0.2 1.5 0.2 1.7 1.2 2.  0.2 1.8 1.5 0.4 2.4]

30% test data:
[[5.9 3.2 4.8 1.8]
 [5.6 3.  4.5 1.5]
 [6.7 3.1 5.6 2.4]
 [5.  3.  1.6 0.2]
 [6.3 2.7 4.9 1.8]
 [6.2 2.2 4.5 1.5]
 [5.3 3.7 1.5 0.2]
 [5.2 4.1 1.5 0.1]
 [6.  2.2 4.  1. ]
 [6.7 3.1 4.4 1.4]
 [5.4 3.7 1.5 0.2]
 [6.4 2.7 5.3 1.9]
 [5.8 2.7 5.1 1.9]
 [7.2 3.6 6.1 2.5]
 [5.9 3.  4.2 1.5]
 [6.4 3.2 5.3 2.3]
 [4.7 3.2 1.6 0.2]
 [5.2 3.5 1.5 0.2]
 [5.7 4.4 1.5 0.4]
 [5.7 2.5 5.  2. ]
 [5.  3.5 1.3 0.3]
 [6.3 2.3 4.4 1.3]
 [6.5 2.8 4.6 1.5]
 [5.4 3.4 1.7 0.2]
 [5.5 3.5 1.3 0.2]
 [7.9 3.8 6.4 2. ]
 [6.4 3.1 5.5 1.8]
 [6.3 3.3 6.  2.5]
 [6.3 2.9 5.6 1.8]
 [4.8 3.4 1.6 0.2]
 [4.9 2.4 3.3 1. ]
 [6.6 3.  4.4 1.4]
 [6.7 3.1 4.7 1.5]
 [6.2 2.8 4.8 1.8]
 [5.5 2.3 4.  1.3]
 [4.9 3.1 1.5 0.1]
 [6.  3.4 4.5 1.6]
 [4.9 3.1 1.5 0.1]
 [5.  3.4 1.6 0.4]
 [5.7 2.8 4.1 1.3]
 [7.2 3.  5.8 1.6]
 [5.7 2.6 3.5 1. ]
 [5.  2.3 3.3 1. ]
 [5.8 2.7 5.1 1.9]
 [7.  3.2 4.7 1.4]]
[1.8 1.5 2.4 0.2 1.8 1.5 0.2 0.1 1.  1.4 0.2 1.9 1.9 2.5 1.5 2.3 0.2 0.2
 0.4 2.  0.3 1.3 1.5 0.2 0.2 2.  1.8 2.5 1.8 0.2 1.  1.4 1.5 1.8 1.3 0.1
 1.6 0.1 0.4 1.3 1.6 1.  1.  1.9 1.4]
PS D:\Work\JIIT\Sem__5\Sem_5>
 """
