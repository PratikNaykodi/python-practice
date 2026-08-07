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

# 1. After training the Decision Tree model, 
# use:
#     model. feature_importances
#     Display importance score of each feature.
#     Which feature contributes the most in predicting FinalResult?
#     Which feature contributes the least?

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Independent Variables (Features)
feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]

# Dependent Variable (Label)
Y = df["FinalResult"]

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create and train Decision Tree model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

# Display Feature Importance
print("Feature Importance")
print("-" * 40)

for feature, importance in zip(feature_cols, model.feature_importances_):
    print(f"{feature:25} : {importance:.4f}")

# Find Most Important Feature
max_index = model.feature_importances_.argmax()
print("\nMost Important Feature :", feature_cols[max_index])

# Find Least Important Feature
min_index = model.feature_importances_.argmin()
print("Least Important Feature :", feature_cols[min_index])