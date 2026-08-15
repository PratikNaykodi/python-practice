# 3. Use KNN to predict whether a student passes or fails based on study hours and attendance.

# Dataset

# Study Hours     Attendance      Result
# 2               60              Fail
# 5               80              Pass
# 6               85              Pass
# 1               50              Fail

# Tasks:
# 1. Accept input from user:

#     1. Study hours
#     2. Attendance percentage
# 2. Apply KNN algorithm
# 3. Predict whether the student Passes or Fails

# Input Example:
# Enter Study Hours: 4
# Enter Attendance: 70

# Expected Output:
# Predicted Result: Pass

import math

# Dataset
data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]


# Function to calculate Euclidean distance
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Function to predict result
def predict(study_hours, attendance, k):

    distances = []

    # Calculate distance from new student to every student
    for hours, attend, result in data:

        distance = calculate_distance(
            study_hours,
            attendance,
            hours,
            attend
        )

        distances.append((distance, result))

    # Sort distances
    distances.sort()

    # Select K nearest neighbors
    nearest = distances[:k]

    # Count votes
    pass_count = 0
    fail_count = 0

    for distance, result in nearest:

        if result == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    # Majority voting
    if pass_count > fail_count:
        return "Pass"
    else:
        return "Fail"


# Accept input from user
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

# K value
k = 3

# Prediction
result = predict(study_hours, attendance, k)

print("\nPredicted Result:", result)
