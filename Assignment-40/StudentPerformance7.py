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

# 7. Train model using:
#     random_state =0
#     random_state = 10
#     random_state = 42

# Compare testing accuracy.
# Does the result change?

# Import required libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Different random_state values
random_states = [0, 10, 42]

print("-" * 50)
print("Testing Accuracy for Different random_state Values")
print("-" * 50)

for state in random_states:

    # Split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=state
    )

    # Create model
    model = DecisionTreeClassifier(random_state=42)

    # Train model
    model.fit(X_train, Y_train)

    # Predict
    Y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    print(f"random_state = {state} --> Testing Accuracy = {accuracy * 100:.2f}%")


# Observation
# random_state = 0
# Testing Accuracy = 83.33%
# random_state = 10
# Testing Accuracy = 83.33%
# random_state = 42
# Testing Accuracy = 100.00%
# Q)Does the result change?
# Answer:
#     Yes, the testing accuracy changes when random_state is changed.
#     This is because random_state changes how the dataset is divided into training and testing sets.
#     Different train-test splits can produce different model performance.
#     In your case, random_state = 42 produced the best split, giving 100% accuracy, while random_state = 0 and 10 resulted in 83.33% accuracy.