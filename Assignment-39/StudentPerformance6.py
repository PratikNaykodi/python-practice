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

# 6. Train three Decision Tree models with:
#     max_depth = 1
#     max_depth = 3
#     max_depth = None
# Compare their testing accuracies and write your observations.

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Different values of max_depth
depths = [1, 3, None]

print("-" * 50)
print("Testing Accuracy for Different max_depth Values")
print("-" * 50)

for depth in depths:

    # Create model
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)

    # Train model
    model.fit(X_train, Y_train)

    # Predict test data
    Y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    print(f"max_depth = {depth} --> Testing Accuracy = {accuracy * 100:.2f}%")

# Observation
# 1. max_depth = 1
#     Testing Accuracy = 100%
#     Even a simple Decision Tree correctly classified all test samples.
# 2. max_depth = 3
#     Testing Accuracy = 100%
#     Increasing the depth did not improve the accuracy because the model was already predicting all test samples correctly.
# 3. max_depth = None
#     Testing Accuracy = 100%
#     Allowing the tree to grow without any depth limit also produced the same accuracy.