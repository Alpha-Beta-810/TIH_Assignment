from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

# 1. Load the digits dataset
digits = load_digits()
X = digits.data

# 2. Initialize the K-Means clustering model
# We set n_clusters=10 because there are 10 distinct digits (0-9)
# random_state is set to ensure reproducibility
kmeans = KMeans(n_clusters=10, random_state=42)

# 3. Fit the model on the features (X)
kmeans.fit(X)

# 4. Assign the resulting cluster labels
kmeans_labels = kmeans.labels_

# Print verification output
print("Successfully fitted model:", kmeans)
print("Cluster labels array shape:", kmeans_labels.shape)
print("First 20 cluster labels:\n", kmeans_labels[:20])