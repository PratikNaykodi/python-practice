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

# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_performance_ml.csv")

# Draw Boxplot
plt.figure(figsize=(6,5))
plt.boxplot(df["Attendance"])

# Add title and labels
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance (%)")

# Display the graph
plt.show()

# Observation
# If no dots appear outside the whiskers, there are no outliers.
# If dots appear outside the whiskers, those attendance values are outliers because they are unusually low or high compared to the rest of the dataset.

# A boxplot is used to visualize the distribution of the Attendance values and detect outliers. The box represents the middle 50% of the data, the line inside the box is the median, and the whiskers show the normal range. Any data points outside the whiskers are considered outliers. Outliers indicate attendance values that are significantly different from the majority of students