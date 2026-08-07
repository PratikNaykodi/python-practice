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

# 6. Plot a histogram of StudyHours.
# Explain what the distribution tells you.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Plot Histogram
plt.figure(figsize=(8,5))
plt.hist(df["StudyHours"], bins=10, edgecolor="black")

# Add title and labels
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

# Display the graph
plt.show()

# Explanation of the Distribution
# A histogram shows how the StudyHours are distributed among students.
# From the histogram, we can observe:
# It shows the number of students studying for different numbers of hours.
# Taller bars indicate that more students fall within that range of study hours.
# Shorter bars indicate that fewer students study that many hours.
# We can identify whether most students study less, average, or more hours per day.
# It also helps detect the presence of outliers or unusual study patterns.