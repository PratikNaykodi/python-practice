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

# 7. Create a scatter plot of:
#     StudyHours vs PreviousScore
#     Use different colors for Pass and Fail students.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Separate Pass and Fail students
pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

# Create Scatter Plot
plt.figure(figsize=(8,6))

plt.scatter(
    pass_students["StudyHours"],
    pass_students["PreviousScore"],
    color="green",
    label="Pass"
)

plt.scatter(
    fail_students["StudyHours"],
    fail_students["PreviousScore"],
    color="red",
    label="Fail"
)

# Add title and labels
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

# Display legend
plt.legend()

# Show graph
plt.show()