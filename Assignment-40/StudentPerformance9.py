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

# 9. Create a new column:
#     PerformanceIndex= (StudyHours * 2) + Attendance

# Train the model including this new feature.
# Does accuracy improve?

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

######################################################
# Step 1 : Load Dataset
######################################################

df = pd.read_csv("student_performance_ml.csv")

######################################################
# Step 2 : Create New Feature
######################################################

# PerformanceIndex = (StudyHours * 2) + Attendance
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

######################################################
# Step 3 : Model Without PerformanceIndex
######################################################

X1 = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X1,
    Y,
    test_size=0.2,
    random_state=42
)

model1 = DecisionTreeClassifier(random_state=42)

model1.fit(X_train, Y_train)

Y_pred = model1.predict(X_test)

accuracy1 = accuracy_score(Y_test, Y_pred)

######################################################
# Step 4 : Model With PerformanceIndex
######################################################

X2 = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]]

X_train, X_test, Y_train, Y_test = train_test_split(
    X2,
    Y,
    test_size=0.2,
    random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)

model2.fit(X_train, Y_train)

Y_pred = model2.predict(X_test)

accuracy2 = accuracy_score(Y_test, Y_pred)

######################################################
# Step 5 : Compare Accuracy
######################################################

print("-" * 50)
print("Accuracy Comparison")
print("-" * 50)

print("Without PerformanceIndex : {:.2f}%".format(accuracy1 * 100))
print("With PerformanceIndex    : {:.2f}%".format(accuracy2 * 100))

print("-" * 50)

if accuracy2 > accuracy1:
    print("Accuracy Improved.")
elif accuracy2 < accuracy1:
    print("Accuracy Decreased.")
else:
    print("Accuracy Remained the Same.")

# Q) Does accuracy improve?
#  Answer:
# No. The testing accuracy remains 100.00% both before and after adding the PerformanceIndex feature. Therefore, the new feature does not improve the model's performance because it is derived from existing features (StudyHours and Attendance), and the Decision Tree can already learn this relationship from the original data.