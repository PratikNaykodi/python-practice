# Machine Learning
# Dataset Description - Student Performance ML 

# Dataset

# The dataset student_performance_ml. csv contains academic and behavioral information of
# students. The objective of this dataset is to predict whether a student will Pass (1) or Fail (0) based on various
# input features.

# Each row in the dataset represents one student, and each column represents a measurable factor that may
# influence academic performance.

# Features Description
#     StudyHours - Number of hours a student studies per day.
#     Attendance - Percentage of class attendance.
#     PreviousScore - Marks obtained in the previous examination.
#     AssignmentsCompleted - Number of assignments completed by the student.
#     SleepHours - Average number of hours the student sleeps per day.
#     FinalResult - Target variable (Output):
#         1 ->Pass
#         0 -> Fail

# Objective of the Dataset
# The goal is to:
#     Build a Machine Learning model to predict whether a student will pass or fail.
#     Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, and model evaluation.
#     Analyze how different factors affect student performance.

#4. Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.

# Explain clearly:    
#     True Positive
#     True Negative
#     False Positive
#     False Negative

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Features (Independent Variables)
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

# Label (Dependent Variable)
Y = df["FinalResult"]

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# Predict the test data
Y_pred = model.predict(X_test)

# Generate Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)

print("Confusion Matrix")
print(cm)

# Display Confusion Matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")
plt.show()

# | Actual \ Predicted | Fail | Pass |
# | ------------------ | ---: | ---: |
# | **Fail**           |   5  |    0 |
# | **Pass**           |   0  |    1 |


# 1. True Positive (TP)

# The student actually passed, and the model also predicted Pass.
# Example:
# Actual = Pass (1)
# Predicted = Pass (1)
# From the above matrix:
# TP = 1

# 2. True Negative (TN)
# The student actually failed, and the model also predicted Fail.
# Example:
# Actual = Fail (0)
# Predicted = Fail (0)
# From the above matrix:
# TN = 5

# 3. False Positive (FP)
# The student actually failed, but the model predicted Pass.
# Example:
# Actual = Fail (0)
# Predicted = Pass (1)
# From the above matrix:
# FP = 0

# 4. False Negative (FN)
# The student actually passed, but the model predicted Fail.
# Example:
# Actual = Pass (1)
# Predicted = Fail (0)
# From the above matrix:
# FN = 0