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

# 5. Based on the dataset values, analyze whether:
#     Higher StudyHours increase the chance of passing.
#     Higher Attendance improves FinalResult.
#     Write your observations in 4-5 lines.

# Import pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Average StudyHours based on FinalResult
study_analysis = df.groupby("FinalResult")["StudyHours"].mean()

# Average Attendance based on FinalResult
attendance_analysis = df.groupby("FinalResult")["Attendance"].mean()

print("===== Average Study Hours =====")
print(study_analysis)

print("\n===== Average Attendance =====")
print(attendance_analysis)

# Observations 
# Students who passed have higher average StudyHours than students who failed.
# Students with higher attendance generally achieve better final results.
# This indicates that StudyHours and Attendance have a positive impact on academic performance.
# Students who study regularly and attend classes consistently are more likely to pass.
# These features are important predictors for building a machine learning model.