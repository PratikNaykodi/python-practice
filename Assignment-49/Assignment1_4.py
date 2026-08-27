# Q4: Write a Python program to calculate the Euclidean distance between two points before and after applying
# feature scaling, and explain the difference in results.
# Answer: 
# Why is there such a big difference?

# Before scaling, Salary has very large values compared with Age. Therefore, Salary dominates the Euclidean distance.

# After applying StandardScaler, both features are put on a similar scale with approximately mean = 0 and standard deviation = 1. Therefore, neither feature dominates the distance simply because of its units.

import numpy as np
from sklearn.preprocessing import StandardScaler

# Two points
P1 = np.array([25, 20000])
P2 = np.array([35, 80000])

# Calculate Euclidean distance before scaling
distance_before = np.sqrt(np.sum((P1 - P2) ** 2))

print("Distance before scaling:", distance_before)

# Dataset used for scaling
data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

# Apply StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Get scaled points
scaled_P1 = scaled_data[0]
scaled_P2 = scaled_data[2]

# Calculate Euclidean distance after scaling
distance_after = np.sqrt(np.sum((scaled_P1 - scaled_P2) ** 2))

print("Distance after scaling:", distance_after)