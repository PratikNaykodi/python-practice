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

# 8. Write a single structured Python program that performs:
#     1. Dataset loading
#     2. Data analysis
#     3. Visualization
#     4. Train-test split
#     5. Model training
#     6. Prediction
#     7. Accuracy calculation
#     8. Confusion matrix generation
#     9. Final conclusion
# Your code should include proper comments explaining each step.

###############################################################
# Student Performance Prediction using Decision Tree
###############################################################

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

Border = "-" * 50

###############################################################
# Step 1 : Load the Dataset
###############################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset Loaded Successfully\n")

print("First 5 Records")
print(df.head())

###############################################################
# Step 2 : Data Analysis (EDA)
###############################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Dataset Shape :", df.shape)

print("\nColumn Names")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nData Types")
print(df.dtypes)

print("\nStatistical Summary")
print(df.describe())

print("\nPass / Fail Distribution")
print(df["FinalResult"].value_counts())

###############################################################
# Step 3 : Data Visualization
###############################################################

print(Border)
print("Step 3 : Visualization")
print(Border)

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

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

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()
plt.grid()

plt.show()

###############################################################
# Step 4 : Prepare Features and Label
###############################################################

print(Border)
print("Step 4 : Features and Label")
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]

Y = df["FinalResult"]

print("Features Shape :", X.shape)
print("Label Shape :", Y.shape)

###############################################################
# Step 5 : Train-Test Split
###############################################################

print(Border)
print("Step 5 : Train-Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("Training Records :", len(X_train))
print("Testing Records :", len(X_test))

###############################################################
# Step 6 : Train Decision Tree Model
###############################################################

print(Border)
print("Step 6 : Train Model")
print(Border)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model Trained Successfully")

###############################################################
# Step 7 : Prediction
###############################################################

print(Border)
print("Step 7 : Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Actual Values")
print(Y_test.values)

print("\nPredicted Values")
print(Y_pred)

###############################################################
# Step 8 : Accuracy and Confusion Matrix
###############################################################

print(Border)
print("Step 8 : Model Evaluation")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy : {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix")

cm = confusion_matrix(Y_test, Y_pred)

print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail","Pass"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")

plt.show()

print("\nClassification Report")
print(classification_report(Y_test, Y_pred))

###############################################################
# Step 9 : Final Conclusion
###############################################################

print(Border)
print("Step 9 : Final Conclusion")
print(Border)

print("Model Accuracy : {:.2f}%".format(accuracy * 100))

if accuracy >= 0.90:
    print("Excellent Model Performance.")
elif accuracy >= 0.75:
    print("Good Model Performance.")
else:
    print("Model Needs Improvement.")

print("\nProject Completed Successfully.")