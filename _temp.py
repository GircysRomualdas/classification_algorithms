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
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

cmap = ListedColormap(['#FF0000', '#008000', '#0000FF'])
plt.figure(figsize=(12, 6))

# Plot raw data
plt.subplot(1, 3, 1)
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap, edgecolors='k', s=20)
plt.title("Raw Data")
plt.xlabel('Feature 2')
plt.ylabel('Feature 3')

# KNN predictions
start_time = timeit.default_timer()
clf = KNN(k=15)
clf.fit(X_train, y_train)
predictions_knn = clf.predict(X_test)
end_time = timeit.default_timer()
acc_knn = accuracy(y_test, predictions_knn)

plt.subplot(1, 3, 2)
plt.scatter(X_test[:, 2], X_test[:, 3], c=predictions_knn, cmap=cmap, edgecolors='k', s=20)
plt.title("K-Nearest Neighbor Predictions")
plt.xlabel('Feature 2')
plt.ylabel('Feature 3')
plt.text(7, 2, f'Accuracy: {acc_knn:.2f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# DecisionTree predictions
start_time = timeit.default_timer()
clf = DecisionTree()
clf.fit(X_train, y_train)
predictions_dt = clf.predict(X_test)
end_time = timeit.default_timer()
acc_dt = accuracy(y_test, predictions_dt)

plt.subplot(1, 3, 3)
plt.scatter(X_test[:, 2], X_test[:, 3], c=predictions_dt, cmap=cmap, edgecolors='k', s=20)
plt.title("DecisionTree Predictions")
plt.xlabel('Feature 2')
plt.ylabel('Feature 3')
plt.text(7, 2, f'Accuracy: {acc_dt:.2f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()

print("\nK-Nearest Neighbor")
print(f"accuracy: {acc_knn}")
print(f"time: {"{:.10f}".format(end_time - start_time)}")

print("\nDecisionTree")
print(f"accuracy: {acc_dt}")
print(f"time: {"{:.10f}".format(end_time - start_time)}")
