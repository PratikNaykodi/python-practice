# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.

# The program should:

# Calculate Euclidean distance

# Sort distances

# · Select K nearest neighbors

# Predict the class based on majority voting

# Dataset

# Point       X       Y     Label

# A           1       2       Red
# B           2       3       Red
# C           3       1       Blue
# D           6       5       Blue

# Tasks

# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.

# Input Format
# Enter X coordinate: 2
# Enter Y coordinate: 2

# Expected Output
# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41

# Predicted Class: Red

import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

distances = []

for point, px, py, label in data:
    distance = calculate_distance(x, y, px, py)
    distances.append((point, distance, label))

distances.sort(key=lambda item: item[1])

nearest = distances[:3]

print("\nNearest Neighbors:")

for point, distance, label in nearest:
    print(point, "-", "Distance:", round(distance, 2))

# Majority voting
red = 0
blue = 0

for point, distance, label in nearest:
    if label == "Red":
        red += 1
    else:
        blue += 1

if red > blue:
    prediction = "Red"
else:
    prediction = "Blue"

print("\nPredicted Class:", prediction)