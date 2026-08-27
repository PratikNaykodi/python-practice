# Q2: Write a Python program that calculates the variance and standard deviation of the dataset:
# [6,7,8,9,10,11, 12]
# Display both results.

import numpy as np

# Dataset
data = [6, 7, 8, 9, 10, 11, 12]

# Calculate variance
variance = np.var(data)

# Calculate standard deviation
standard_deviation = np.std(data)

# Display results
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)