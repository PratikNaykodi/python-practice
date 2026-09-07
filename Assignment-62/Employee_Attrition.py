# Deep Learning Assignment

# A software company is experiencing high employee turnover. Management wants to build an intelligent system
# that can identify employees who are likely to leave the company.

# The HR department has collected historical employee information.

# Dataset

# Create a CSV file named:

# Employee_Attrition.csv

# Possible features:

# Feature                     Description
# 1. Age                     - Employee age
# 2. MonthlyIncome           - Monthly salary
# 3. YearsAtCompany          - Experience in current company
# 4. TotalWorkingYears       - Total professional experience
# 5. DistanceFromHome        - Distance from home to office
# 6. JobSatisfaction         - Rating from 1-4
# 7. WorkLifeBalance         - Rating from 1-4
# 8. OverTime                - Yes/No
# 9. NumCompaniesWorked      - Previous companies
# 10. TrainingTimesLastYear  - Number of trainings
# 11. Attrition              - Yes/No - Target


# Assignment

# Build a Deep Learning-based Employee Attrition Prediction System using MLPClassifier.
# The system should accept employee information and predict:
#     0 - Employee is likely to stay
#     1 - Employee is likely to leave

# Tasks

# 1. Load the dataset using Pandas.
# 2. Display the shape, columns and first five records.
# 3. Check for missing values.
# 4. Identify numerical and categorical features.
# 5. Convert categorical features such as OverTime into numerical representation.
# 6. Convert the target Attrition into 0 and 1.
# 7. Separate independent and dependent variables.
# 8. Divide the dataset into training and testing data.
# 9. Apply appropriate feature scaling.
# 10. Design an MLP with at least two hidden layers.
# 11. Train the network.
# 12. Display the number of iterations required for training.
# 13. Calculate training accuracy.
# 14. Calculate testing accuracy.
# 15. Generate a confusion matrix.
# 16. Plot the loss curve.
# 17. Create a function: PredictAttrition(employee_data)
# 18. Test the system using at least five new employee records.
# 19. Explain whether the model is suffering from overfitting or underfitting.


# Deep Learning Assignment
# Employee Attrition Prediction using MLPClassifier

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# ------------------------------------------------------------
# 1. Load the dataset using Pandas
# ------------------------------------------------------------

df = pd.read_csv("Employee_Attrition.csv")

print("Dataset loaded successfully!")

# ------------------------------------------------------------
# 2. Display shape, columns and first five records
# ------------------------------------------------------------

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst Five Records:")
print(df.head())

# ------------------------------------------------------------
# 3. Check for missing values
# ------------------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------------------------
# 4. Identify numerical and categorical features
# ------------------------------------------------------------

numerical_features = df.select_dtypes(
    include=np.number
).columns

categorical_features = df.select_dtypes(
    exclude=np.number
).columns

print("\nNumerical Features:")
print(numerical_features)

print("\nCategorical Features:")
print(categorical_features)

# ------------------------------------------------------------
# 5. Convert categorical feature OverTime into numerical
# ------------------------------------------------------------

df["OverTime"] = df["OverTime"].map({
    "Yes": 1,
    "No": 0
})

print("\nAfter converting OverTime:")
print(df.head())

# ------------------------------------------------------------
# 6. Convert target Attrition into 0 and 1
# ------------------------------------------------------------

df["Attrition"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})

print("\nAfter converting Attrition:")
print(df.head())

# ------------------------------------------------------------
# 7. Separate independent and dependent variables
# ------------------------------------------------------------

X = df.drop("Attrition", axis=1)

Y = df["Attrition"]

print("\nIndependent Variables X:")
print(X.head())

print("\nDependent Variable Y:")
print(Y.head())

# ------------------------------------------------------------
# 8. Divide dataset into training and testing data
# ------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

# ------------------------------------------------------------
# 9. Apply feature scaling
# ------------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("\nFeature Scaling Completed")

# ------------------------------------------------------------
# 10. Design MLP with at least two hidden layers
# ------------------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print("\nMLP Model Created")

# ------------------------------------------------------------
# 11. Train the network
# ------------------------------------------------------------

model.fit(
    X_train_scaled,
    Y_train
)

print("\nModel Training Completed")

# ------------------------------------------------------------
# 12. Display number of iterations
# ------------------------------------------------------------

print("\nNumber of Iterations Required:")
print(model.n_iter_)

# ------------------------------------------------------------
# 13. Calculate training accuracy
# ------------------------------------------------------------

Y_train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)

print("\nTraining Accuracy:")
print(train_accuracy)

print("Training Accuracy Percentage:",
      train_accuracy * 100)

# ------------------------------------------------------------
# 14. Calculate testing accuracy
# ------------------------------------------------------------

Y_test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(
    Y_test,
    Y_test_pred
)

print("\nTesting Accuracy:")
print(test_accuracy)

print("Testing Accuracy Percentage:",
      test_accuracy * 100)

# ------------------------------------------------------------
# 15. Generate confusion matrix
# ------------------------------------------------------------

cm = confusion_matrix(
    Y_test,
    Y_test_pred
)

print("\nConfusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Stay", "Leave"]
)

display.plot()

plt.title("Employee Attrition Confusion Matrix")

plt.show()

# ------------------------------------------------------------
# 16. Plot the loss curve
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    model.loss_curve_
)

plt.xlabel("Iterations")

plt.ylabel("Loss")

plt.title("MLP Training Loss Curve")

plt.grid()

plt.show()

# ------------------------------------------------------------
# 17. Create PredictAttrition(employee_data) function
# ------------------------------------------------------------

def PredictAttrition(employee_data):

    # Convert dictionary into DataFrame

    employee_df = pd.DataFrame(
        [employee_data]
    )

    # Convert OverTime into numerical value

    employee_df["OverTime"] = employee_df[
        "OverTime"
    ].map({
        "Yes": 1,
        "No": 0
    })

    # Scale the input data

    employee_scaled = scaler.transform(
        employee_df
    )

    # Predict

    prediction = model.predict(
        employee_scaled
    )

    # Convert prediction into readable result

    if prediction[0] == 1:

        return "1 - Employee is likely to leave"

    else:

        return "0 - Employee is likely to stay"

# ------------------------------------------------------------
# 18. Test using five new employee records
# ------------------------------------------------------------

employee1 = {
    "Age": 25,
    "MonthlyIncome": 25000,
    "YearsAtCompany": 1,
    "TotalWorkingYears": 2,
    "DistanceFromHome": 30,
    "JobSatisfaction": 1,
    "WorkLifeBalance": 1,
    "OverTime": "Yes",
    "NumCompaniesWorked": 5,
    "TrainingTimesLastYear": 2
}

employee2 = {
    "Age": 45,
    "MonthlyIncome": 90000,
    "YearsAtCompany": 15,
    "TotalWorkingYears": 20,
    "DistanceFromHome": 5,
    "JobSatisfaction": 4,
    "WorkLifeBalance": 4,
    "OverTime": "No",
    "NumCompaniesWorked": 2,
    "TrainingTimesLastYear": 5
}

employee3 = {
    "Age": 30,
    "MonthlyIncome": 40000,
    "YearsAtCompany": 3,
    "TotalWorkingYears": 6,
    "DistanceFromHome": 25,
    "JobSatisfaction": 2,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "NumCompaniesWorked": 4,
    "TrainingTimesLastYear": 1
}

employee4 = {
    "Age": 50,
    "MonthlyIncome": 120000,
    "YearsAtCompany": 20,
    "TotalWorkingYears": 28,
    "DistanceFromHome": 3,
    "JobSatisfaction": 4,
    "WorkLifeBalance": 4,
    "OverTime": "No",
    "NumCompaniesWorked": 1,
    "TrainingTimesLastYear": 6
}

employee5 = {
    "Age": 28,
    "MonthlyIncome": 35000,
    "YearsAtCompany": 2,
    "TotalWorkingYears": 4,
    "DistanceFromHome": 40,
    "JobSatisfaction": 1,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "NumCompaniesWorked": 7,
    "TrainingTimesLastYear": 1
}

print("\nEmployee 1:")
print(PredictAttrition(employee1))

print("\nEmployee 2:")
print(PredictAttrition(employee2))

print("\nEmployee 3:")
print(PredictAttrition(employee3))

print("\nEmployee 4:")
print(PredictAttrition(employee4))

print("\nEmployee 5:")
print(PredictAttrition(employee5))

# ------------------------------------------------------------
# 19. Check Overfitting / Underfitting
# ------------------------------------------------------------

print("\nModel Evaluation:")

difference = train_accuracy - test_accuracy

print("Difference between Training and Testing Accuracy:",
      difference)

if difference > 0.10:

    print("Model may be suffering from Overfitting.")

elif train_accuracy < 0.70 and test_accuracy < 0.70:

    print("Model may be suffering from Underfitting.")

else:

    print("Model has reasonable generalization.")