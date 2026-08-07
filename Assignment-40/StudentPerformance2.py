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

# 2. Remove the column SleepHours from the dataset.
#     Train the model again.
#     Compare new accuracy with previous accuracy.
#     Does removing this feature affect performance?

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

######################################################
# Model 1 : With SleepHours
######################################################

print("-" * 50)
print("Model 1 : With SleepHours")
print("-" * 50)

X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy1 = accuracy_score(Y_test, Y_pred)

print("Accuracy with SleepHours : {:.2f}%".format(accuracy1 * 100))

######################################################
# Model 2 : Without SleepHours
######################################################

print("-" * 50)
print("Model 2 : Without SleepHours")
print("-" * 50)

X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy2 = accuracy_score(Y_test, Y_pred)

print("Accuracy without SleepHours : {:.2f}%".format(accuracy2 * 100))

######################################################
# Comparison
######################################################

print("-" * 50)
print("Comparison")
print("-" * 50)

if accuracy1 > accuracy2:
    print("Removing SleepHours reduced the model accuracy.")
    print("SleepHours is an important feature.")
elif accuracy1 < accuracy2:
    print("Removing SleepHours improved the model accuracy.")
    print("SleepHours is not very useful.")
else:
    print("Accuracy remains the same.")
    print("Removing SleepHours does not affect the model performance.")