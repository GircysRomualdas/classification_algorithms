from sklearn import datasets 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import timeit
from knn import KNN
from decisionTree import DecisionTree


def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)


# load test dataset
iris = datasets.load_wine()
#iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

cmap = ListedColormap(['#FF0000', '#008000', '#0000FF'])
plt.figure()
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap, edgecolors='k', s=20, label='Training Data')
plt.show()

start_time = timeit.default_timer()
clf = KNN(k=15)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
end_time = timeit.default_timer()
acc = accuracy(y_test, predictions)

print("\nK-Nearest Neighbor")
print(f"accuracy: {acc}")
print(f"time: {"{:.10f}".format(end_time - start_time)}")


start_time = timeit.default_timer()
clf = DecisionTree()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
end_time = timeit.default_timer()
acc = accuracy(y_test, predictions)

print("\nDecisionTree")
print(f"accuracy: {acc}")
print(f"time: {"{:.10f}".format(end_time - start_time)}")