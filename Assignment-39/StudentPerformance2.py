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

# 2. Use the trained model to predict results for X_test.
#     Display predicted values along with actual values.

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Independent variables (Features)
X = df[[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]]

# Dependent variable (Label)
Y = df["FinalResult"]

# Split dataset into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, Y_train)

# Predict the results for X_test
Y_pred = model.predict(X_test)

# Display Actual and Predicted values
result = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": Y_pred
})

print(result)