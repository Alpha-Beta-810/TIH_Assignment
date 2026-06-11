from sklearn.datasets import load_digits

# Load the digits dataset
digits = load_digits()

# Separate the dataset into features (X) and target labels (y)
X = digits.data
y = digits.target

# Print the shape of the features and target arrays
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)