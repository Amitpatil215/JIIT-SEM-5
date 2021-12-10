from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris= load_iris()

x=iris.data
y=iris.target
print(x)
print(y)

feature_names = iris.feature_names
target_names = iris.target_names
print("Feature names:", feature_names)
print("Target names:", target_names)
print("\nFirst 10 rows of X:\n", x[:10])

iris = load_iris()

X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)
