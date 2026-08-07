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

# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Calculate average SleepHours for Pass and Fail
sleep_avg = df.groupby("FinalResult")["SleepHours"].mean()

# Create Bar Chart
plt.figure(figsize=(6,5))

plt.bar(
    ["Fail", "Pass"],
    sleep_avg,
    color=["red", "green"]
)

# Add title and labels
plt.title("Average Sleep Hours vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Sleep Hours")

# Display values on top of bars
for i, value in enumerate(sleep_avg):
    plt.text(i, value + 0.05, f"{value:.2f}", ha="center")

plt.show()


# Does Sleeping More Guarantee Success?
# Answer: No.
# Sleeping more does not guarantee success.
# For example:
# Student A sleeps 8 hours but studies only 1 hour and has poor attendance.
# Student B sleeps 7 hours, studies 6 hours, attends classes regularly, and completes assignments.
# Student B is more likely to pass, even though they sleep slightly less.
# So, adequate sleep is important, but success depends on a balance of study habits, attendance, previous performance, assignments, and sleep.