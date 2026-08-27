# Q3: Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000],
# [30,40000],
# [35,80000]]
# Print the scaled dataset.

from sklearn.preprocessing import StandardScaler

# Dataset
data = [
    [25, 20000],
    [30, 40000],
    [35, 80000]
]

# Create StandardScaler object
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

# Print scaled dataset
print("Scaled Dataset:")
print(scaled_data)