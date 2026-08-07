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

# 1. Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
#     First 5 records
#     Last 5 records
#     Total number of rows and columns
#     List of column names
#     Data types of each column

# Import pandas library
import pandas as pd

# Load the CSV file
df = pd.read_csv("student_performance_ml.csv")

# Display first 5 records
print("===== First 5 Records =====")
print(df.head())

# Display last 5 records
print("\n===== Last 5 Records =====")
print(df.tail())

# Display total number of rows and columns
print("\n===== Dataset Shape =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display column names
print("\n===== Column Names =====")
print(df.columns.tolist())

# Display data types
print("\n===== Data Types =====")
print(df.dtypes)