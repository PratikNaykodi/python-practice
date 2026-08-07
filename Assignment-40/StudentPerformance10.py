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

# 10. Train model with:
#     max_depth = None
#     Calculate:
#         Training accuracy
#         Testing accuracy

# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

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
# Step 2 : Select Features and Label
######################################################

X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

Y = df["FinalResult"]

######################################################
# Step 3 : Split Dataset
######################################################

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

######################################################
# Step 4 : Create Decision Tree Model
######################################################

model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

######################################################
# Step 5 : Train Model
######################################################

model.fit(X_train, Y_train)

######################################################
# Step 6 : Training Prediction
######################################################

Y_train_pred = model.predict(X_train)

######################################################
# Step 7 : Testing Prediction
######################################################

Y_test_pred = model.predict(X_test)

######################################################
# Step 8 : Calculate Accuracy
######################################################

train_accuracy = accuracy_score(Y_train, Y_train_pred)

test_accuracy = accuracy_score(Y_test, Y_test_pred)

print("-" * 50)
print("Decision Tree (max_depth = None)")
print("-" * 50)

print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))


# Q). If training accuracy is 100% but testing accuracy is lower, explain why this happens.
# Answer:
# If the training accuracy is 100% but the testing accuracy is lower, it means the model is overfitting.

# Why does this happen?
# The Decision Tree has learned the training data too perfectly, including noise and unnecessary details.
# Instead of learning general patterns, it memorizes the training data.
# When new (unseen) test data is given, the model cannot predict as accurately because it has not learned to generalize.
# This results in high training accuracy but lower testing accuracy.