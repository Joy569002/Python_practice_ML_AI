import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from math import sqrt
from machine_learning.Algorithm_implemention.Basic_algorithm.KNN.knn import KNN  # Your custom KNN class

# 🔹 Dynamically generate a colormap based on number of classes
def get_dynamic_cmap(n_classes, base='tab10'):
    base_cmap = plt.cm.get_cmap(base)
    colors = base_cmap.colors[:n_classes]
    return ListedColormap(colors)

# 🔹 Load and return dataset
def load_data():
    iris = datasets.load_iris()
    return iris.data, iris.target

# 🔹 Visualize selected features with dynamic color mapping
def visualize_data(X, y, feature_indices=(2, 3), cmap=None):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, feature_indices[0]], X[:, feature_indices[1]],
                c=y, cmap=cmap, edgecolor='k', s=50)
    plt.xlabel(f"Feature {feature_indices[0]}")
    plt.ylabel(f"Feature {feature_indices[1]}")
    plt.title("Iris Dataset Visualization")
    plt.grid(True)
    plt.show()

# 🔹 Dynamically compute k using rule of thumb
def dynamic_k(X):
    return round(sqrt(len(X)))

# 🔹 Run k-NN and return predictions + accuracy
def run_knn(X, y, test_size=0.2, random_state=1234):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=test_size,
                                                        random_state=random_state)
    k = dynamic_k(X_train)
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    return predictions, accuracy, y_test

# 🔹 Main execution block
def main():
    X, y = load_data()
    cmap = get_dynamic_cmap(len(np.unique(y)))
    visualize_data(X, y, feature_indices=(2, 3), cmap=cmap)

    predictions, acc, y_test = run_knn(X, y)
    print("🔍 Predictions:")
    for i, pred in enumerate(predictions):
        print(f"Sample {i}: Predicted = {pred}, Actual = {y_test[i]}")
    print(f"\n✅ Accuracy: {acc:.2f}")

if __name__ == "__main__":
    main()