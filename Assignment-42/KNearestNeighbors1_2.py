# 2. The value of K plays an important role in the KNN algorithm.

# Write a Python program that demonstrates how prediction changes when K changes.

# Dataset
# Use the same dataset as Assignment 1.

# Tasks

# Predict the class of the same new point using:
# K=1
# K=3
# K=5

# Expected Output

# Prediction Results
# K = 1 - Red
# K = 3 - Red
# K = 5 - Blue

# Explain why the prediction changes when K increases.
#Answer:  As the value of K increases, KNN considers more neighboring data points for classification. The additional neighbors may belong to a different class, which can change the majority vote and therefore change the prediction. A small K is more sensitive to nearby points, while a larger K gives a more general prediction based on more neighbors.

# Yes. Since our dataset has only 4 points, there is one important issue: K = 5 is not possible because K cannot be greater than the number of data points.

# To get the expected output:

# K = 1 - Red
# K = 3 - Red
# K = 5 - Blue

# you need at least 5 data points. If your assignment says "same dataset as Assignment 1", then the expected K=5 output is inconsistent with the 4-point dataset.

import math

# Dataset
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]


# Function to calculate Euclidean distance
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Function to predict class
def predict(x, y, k):

    distances = []

    # Calculate distance from every point
    for point, px, py, label in data:

        distance = calculate_distance(x, y, px, py)

        distances.append((point, distance, label))

    # Sort based on distance
    distances.sort(key=lambda item: item[1])

    # Select K nearest neighbors
    nearest = distances[:k]

    # Count votes
    votes = {}

    for point, distance, label in nearest:

        if label not in votes:
            votes[label] = 0

        votes[label] += 1

    # Find majority class
    prediction = max(votes, key=votes.get)

    return prediction


# New point
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))


print("\nPrediction Results")

# K = 1
prediction = predict(x, y, 1)
print("K = 1 -", prediction)

# K = 3
prediction = predict(x, y, 3)
print("K = 3 -", prediction)

# K = 4
prediction = predict(x, y, 4)
print("K = 4 -", prediction)