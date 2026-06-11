import numpy as np
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.metrics import f1_score
from scipy.stats import mode

# 1. Load the digits dataset and separate features and target labels
digits = load_digits()
X = digits.data
y = digits.target

# 2. Initialize and fit the K-Means clustering model (10 clusters)
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(X)
kmeans_labels = kmeans.labels_

# 3. Map each cluster label to the most frequent true label in that cluster
mapped_labels = np.zeros_like(kmeans_labels)

for i in range(10):
    # Mask to identify samples belonging to cluster i
    mask = (kmeans_labels == i)
    
    if np.sum(mask) > 0:
        # Find the most frequent true digit label within this cluster partition
        most_common_true_label = mode(y[mask], keepdims=True).mode[0]
        # Assign this true label back to the corresponding indices
        mapped_labels[mask] = most_common_true_label

# 4. Calculate and print the macro-averaged F1 score
f1 = f1_score(y, mapped_labels, average='macro')
print(f"Calculated Macro-Averaged F1 Score: {f1:.4f}")