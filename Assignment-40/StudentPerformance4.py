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

# 4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# diplay predictions clearly.

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

#########################################################
# New Students Data
#########################################################

new_students = pd.DataFrame({

    "StudyHours" : [6, 2, 5, 8, 4],
    "Attendance" : [85, 55, 75, 95, 65],
    "PreviousScore" : [66, 40, 58, 88, 52],
    "AssignmentsCompleted" : [7, 3, 6, 10, 5],
    "SleepHours" : [7, 6, 8, 7, 5]

})

#########################################################
# Predict Results
#########################################################

prediction = model.predict(new_students)

# Add prediction to DataFrame
new_students["Prediction"] = prediction

# Convert 0/1 into Fail/Pass
new_students["Prediction"] = new_students["Prediction"].map({
    1: "Pass",
    0: "Fail"
})

#########################################################
# Display Results
#########################################################

print("Prediction of New Students")
print("-" * 60)

print(new_students)