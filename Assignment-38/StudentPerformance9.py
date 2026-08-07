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

# 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Calculate average assignments completed for Pass and Fail
assignment_avg = df.groupby("FinalResult")["AssignmentsCompleted"].mean()

# Create Bar Chart
plt.figure(figsize=(6,5))

plt.bar(
    ["Fail", "Pass"],
    assignment_avg,
    color=["red", "green"]
)

# Add title and labels
plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Assignments Completed")

# Display values on top of bars
for i, value in enumerate(assignment_avg):
    plt.text(i, value + 0.1, f"{value:.2f}", ha='center')

plt.show()

# Observation
# Students who passed generally completed more assignments than students who failed.
# Students who completed fewer assignments were more likely to fail.
# This indicates a positive relationship between assignment completion and academic performance.
# Completing assignments regularly improves the chances of passing.
# Therefore, AssignmentsCompleted is an important feature for predicting the FinalResult.