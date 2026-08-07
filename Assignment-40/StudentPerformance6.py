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

# 6. Identify students where:
#     y_test != y_pred
#         Display those rows.
#         How many students were misclassified?
#         What common pattern do you observe?

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

# Create and train model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

# Predict test data
Y_pred = model.predict(X_test)

##########################################################
# Find Misclassified Students
##########################################################

# Create a copy of test data
result = X_test.copy()

# Add Actual and Predicted values
result["Actual"] = Y_test.values
result["Predicted"] = Y_pred

# Display only misclassified students
misclassified = result[result["Actual"] != result["Predicted"]]

print("Misclassified Students")
print("-" * 50)
print(misclassified)

print("\nTotal Misclassified Students :", len(misclassified))

# Observation
# If there are misclassified students:
# These are the students for whom the model made incorrect predictions.
# They often have feature values that are close to the decision boundary or have mixed characteristics.

# If there are no misclassified students:
# The model correctly classified every student in the test set.
# Total Misclassified Students = 0.