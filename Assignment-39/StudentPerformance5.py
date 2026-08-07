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

# 5. Calculate:
#     Training accuracy
#     Testing accuracy
#     Compare both and comment whether the model is overfitting or underfitting.

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

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, Y_train)

# Predict Training Data
Y_train_pred = model.predict(X_train)

# Predict Testing Data
Y_test_pred = model.predict(X_test)

# Calculate Training Accuracy
train_accuracy = accuracy_score(Y_train, Y_train_pred)

# Calculate Testing Accuracy
test_accuracy = accuracy_score(Y_test, Y_test_pred)

# Display Accuracy
print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))

# Compare Accuracy
if train_accuracy > test_accuracy + 0.10:
    print("\nModel is Overfitting.")
elif train_accuracy < test_accuracy:
    print("\nModel may be Underfitting.")
else:
    print("\nModel is Well Fitted.")

# Is the model overfitting?
# Answer: No.

# Output
# Training Accuracy = 100%
# Testing Accuracy  = 100%

# Both accuracies are equal, so there is no evidence of overfitting or underfitting based on these results.

# Comment:
# The model achieved 100% accuracy on both the training and testing datasets. Since both accuracies are equal, the model appears to be well-fitted and made correct predictions for all samples in both datasets.