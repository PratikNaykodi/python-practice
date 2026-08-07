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

# 4. Use value_counts () to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

# Import pandas library
import pandas as pd

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Count Pass and Fail students
result = df["FinalResult"].value_counts()

print("===== FinalResult Distribution =====")
print(result)

# Calculate percentages
percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\n===== Percentage Distribution =====")
print(percentage)

# Display individually
print("\nPass Percentage : {:.2f}%".format(percentage[1]))
print("Fail Percentage : {:.2f}%".format(percentage[0]))

# Check whether dataset is balanced
if abs(percentage[1] - percentage[0]) <= 10:
    print("\nDataset Status : Balanced Dataset")
else:
    print("\nDataset Status : Imbalanced Dataset")


# Is the dataset balanced?
# Answer:
# A dataset is considered balanced when all classes have approximately the same number of samples.
# For example:
#     Pass = 50%
#     Fail = 50%
#     or close to that (e.g., 48%–52%).
#     If one class has significantly more samples than the other, the dataset is imbalanced.

# Example
#     Pass = 72%
#     Fail = 28%
#     This is an imbalanced dataset because there are many more passing students than failing students.