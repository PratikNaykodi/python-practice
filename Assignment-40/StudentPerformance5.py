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

# 5. Without using accuracy_score, manually calculate accuracy:
#     Verify whether it matches sklearn accuracy.

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

# Create and train model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

# Predict results
Y_pred = model.predict(X_test)

#########################################################
# Manual Accuracy Calculation
#########################################################

# Count correct predictions
correct_predictions = (Y_test == Y_pred).sum()

# Total test samples
total_predictions = len(Y_test)

# Manual accuracy
manual_accuracy = (correct_predictions / total_predictions) * 100

print("Correct Predictions :", correct_predictions)
print("Total Predictions   :", total_predictions)
print("Manual Accuracy     : {:.2f}%".format(manual_accuracy))

#########################################################
# Accuracy using sklearn
#########################################################

sklearn_accuracy = accuracy_score(Y_test, Y_pred) * 100

print("Sklearn Accuracy    : {:.2f}%".format(sklearn_accuracy))