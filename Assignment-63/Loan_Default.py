# Deep Learning Assignment

# A bank provides personal loans to customers. Some customers fail to repay their loans.
# The bank wants to develop a Deep Learning system that predicts whether a new applicant has a high probability
# of defaulting on the loan.
# This prediction will help the bank assess risk before approving loans.

# Dataset:

# Feature                        Description
# 1. Age                         - Applicant age
# 2. Income                      - Annual income
# 3. LoanAmount                  - Requested loan
# 4. CreditScore                 - Credit score
# 5. Employment Years            - Years employed
# 6. ExistingLoans               - Number of existing loans
# 7. MonthlyDebt                 - Existing monthly debt
# 8. LoanTerm                    - Loan duration
# 9. PreviousDefault             - Yes/No
# 10. HomeOwnership              - Rent/Own/Mortgage
# 11. Default                    - 0/1 - Target

# Build:
# Loan Default Prediction using Multi-Layer Perceptron
# Output:
#     0 -> Low default risk
#     1 -> High default risk

# Tasks:
# 1. Load and understand the dataset.
# 2. Perform exploratory analysis.
# 3. Find missing values.
# 4. Check whether the target classes are balanced.
# 5. Encode categorical variables.
# 6. Separate X and y.
# 7. Split the dataset into training and testing data.
# 8. Explain whether stratified splitting should be used.
# 9. Scale the features.
# 10. Create an MLPClassifier.
#     Start with:
#         MLPClassifier(
#             hidden_layer_sizes=(32, 16),
#             activation='relu',
#             solver='adam',
#             max_iter=1000,
#             random state=42
#         )
# 11. Train the model.
# 12. Calculate accuracy.
# 13. Generate the confusion matrix.
# 14. Generate the classification report.
# 15. Calculate precision, recall and F1-score.
# 16. Plot training loss.
# 17. Test the model on new loan applicants.

# Hyperparameter Experiment:
# Change one parameter at a time.
# Experiment 1 - Activation
#     identity
#     logistic
#     tanh
#     relu

# Experiment 2 - Hidden Layers
#     (10,)
#     (20,10)
#     (50,25)
#     (100,50,25)

# Experiment 3 - Learning Rate
# Try different values for learning_rate_init.

# ------------------------------------------------------------
# Deep Learning Assignment
# Loan Default Prediction Using Mlpclassifier
# ------------------------------------------------------------

# ------------------------------------------------------------
# Import Libraries
# ------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

# ------------------------------------------------------------
# 1. Load And Understand The Dataset
# ------------------------------------------------------------
df = pd.read_csv("Loan_Default.csv")

print("------------------------------------------------------------")
print("Dataset")
print("------------------------------------------------------------")

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------------------------
# 2. Exploratory Data Analysis
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Exploratory Data Analysis")
print("------------------------------------------------------------")

print("\nDefault Value Counts:")
print(df["Default"].value_counts())

print("\nDefault Percentage:")
print(df["Default"].value_counts(normalize=True) * 100)

# Plot target distribution

plt.figure(figsize=(6, 4))
df["Default"].value_counts().plot(kind="bar")
plt.xlabel("Default")
plt.ylabel("Number of Applicants")
plt.title("Loan Default Distribution")
plt.xticks(rotation=0)
plt.show()

# ------------------------------------------------------------
# 3. Find Missing Values
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Missing Values")
print("------------------------------------------------------------")

print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# ------------------------------------------------------------
# 4. Check Whether Target Classes Are Balanced
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Target Class Balance")
print("------------------------------------------------------------")

class_counts = df["Default"].value_counts()

print("\nClass Counts:")
print(class_counts)

class_percentage = df["Default"].value_counts(
    normalize=True
) * 100

print("\nClass Percentage:")
print(class_percentage)

# Check balance
difference = abs(
    class_percentage.iloc[0] -
    class_percentage.iloc[1]
)

if difference <= 10:
    print("\nTarget classes are approximately balanced.")
else:
    print("\nTarget classes are imbalanced.")

# ------------------------------------------------------------
# 5. Encode Categorical Variables
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Encoding Categorical Variables")
print("------------------------------------------------------------")

# PreviousDefault
# Yes = 1
# No = 0

df["PreviousDefault"] = df["PreviousDefault"].map({
    "Yes": 1,
    "No": 0
})

# HomeOwnership
# Rent / Own / Mortgage
# Convert using One-Hot Encoding

df = pd.get_dummies(
    df,
    columns=["HomeOwnership"],
    dtype=int
)

print("\nDataset After Encoding:")
print(df.head())

print("\nColumns After Encoding:")
print(df.columns)

# ------------------------------------------------------------
# 6. Separate X And Y
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Separating X And Y")
print("------------------------------------------------------------")

X = df.drop("Default",axis=1)

y = df["Default"]

print("\nIndependent Variables X:")
print(X.head())

print("\nDependent Variable y:")
print(y.head())

print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)

# ------------------------------------------------------------
# 7. Split Data Into Training And Testing
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("TRAIN TEST SPLIT")
print("------------------------------------------------------------")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining Data:")
print(X_train.shape)

print("\nTesting Data:")
print(X_test.shape)

# ------------------------------------------------------------
# 8. Explanation Of Stratified Splitting
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Stratified SplittinG")
print("------------------------------------------------------------")

print("""
Stratified splitting should be used because the
Default target may be imbalanced.

stratify=y maintains approximately the same
proportion of Default=0 and Default=1 in both
training and testing datasets.
""")

# ------------------------------------------------------------
# 9. Feature Scaling
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Feature Scaling")
print("------------------------------------------------------------")

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("Feature scaling completed.")

# ------------------------------------------------------------
# 10. Create MLP Classifier
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("MLP Classifier")
print("------------------------------------------------------------")

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)
print(model)

# ------------------------------------------------------------
# 11. Train The Model
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Model Training")
print("------------------------------------------------------------")
model.fit(X_train_scaled,y_train)
print("Model training completed.")

# ------------------------------------------------------------
# 12. Number Of Iterations
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Number Of Iterations")
print("------------------------------------------------------------")
print("Number of iterations required:",model.n_iter_)

# ------------------------------------------------------------
# 13. Training Accuracy
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Training Accuracy")
print("------------------------------------------------------------")
y_train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(y_train,y_train_pred)

print("Training Accuracy:",train_accuracy)
print("Training Accuracy Percentage:",train_accuracy * 100)

# ------------------------------------------------------------
# 14. Testing Accuracy
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Testing Accuracy")
print("------------------------------------------------------------")
y_test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(y_test,y_test_pred)

print("Testing Accuracy:",test_accuracy)

print("Testing Accuracy Percentage:",test_accuracy * 100)

# ------------------------------------------------------------
# 15. Confusion Matrix
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Confusion Matrix")
print("------------------------------------------------------------")
cm = confusion_matrix(y_test,y_test_pred)

print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "Low Risk",
        "High Risk"
    ]
)
disp.plot()
plt.title("Loan Default Confusion Matrix")
plt.show()

# ------------------------------------------------------------
# 16. Classification Report
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Classification Report")
print("------------------------------------------------------------")
print(
    classification_report(
        y_test,
        y_test_pred,
        target_names=[
            "Low Risk",
            "High Risk"
        ]
    )
)

# ------------------------------------------------------------
# 17. Precision
# ------------------------------------------------------------
precision = precision_score(y_test,y_test_pred,zero_division=0)
print("\nPrecision:")
print(precision)

# ------------------------------------------------------------
# 18. Recall
# ------------------------------------------------------------
recall = recall_score(y_test,y_test_pred,zero_division=0)

print("\nRecall:")
print(recall)

# ------------------------------------------------------------
# 19. F1 Score
# ------------------------------------------------------------
f1 = f1_score(y_test,y_test_pred,zero_division=0)

print("\nF1-Score:")
print(f1)

# ------------------------------------------------------------
# 20. Training Loss Curve
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Training Loss Curve")
print("------------------------------------------------------------")
plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.grid()
plt.show()

# ------------------------------------------------------------
# 21. Prediction Function
# ------------------------------------------------------------
def PredictLoanDefault(applicant_data):
    # Convert dictionary into DataFrame
    applicant_df = pd.DataFrame(
        [applicant_data]
    )

    # Convert PreviousDefault
    applicant_df["PreviousDefault"] = (
        applicant_df["PreviousDefault"].map({
            "Yes": 1,
            "No": 0
        })
    )

    # Convert HomeOwnership
    applicant_df = pd.get_dummies(
        applicant_df,
        columns=["HomeOwnership"],
        dtype=int
    )

    # Make sure columns are exactly the same
    # as training data
    applicant_df = applicant_df.reindex(columns=X.columns,fill_value=0)

    # Apply scaling
    applicant_scaled = scaler.transform(applicant_df)

    # Make prediction
    prediction = model.predict(applicant_scaled)[0]

    # Calculate probability
    probability = model.predict_proba(applicant_scaled)[0][1]

    # Return result
    if prediction == 1:
        return ("1 - High Default Risk",probability)
    else:
        return ("0 - Low Default Risk",probability)

# ------------------------------------------------------------
# 22. Test Five New Loan Applicants
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("New Applicant Predictions")
print("------------------------------------------------------------")

applicant1 = {
    "Age": 25,
    "Income": 300000,
    "LoanAmount": 500000,
    "CreditScore": 580,
    "EmploymentYears": 1,
    "ExistingLoans": 4,
    "MonthlyDebt": 30000,
    "LoanTerm": 60,
    "PreviousDefault": "Yes",
    "HomeOwnership": "Rent"
}

applicant2 = {
    "Age": 45,
    "Income": 1200000,
    "LoanAmount": 300000,
    "CreditScore": 780,
    "EmploymentYears": 15,
    "ExistingLoans": 1,
    "MonthlyDebt": 10000,
    "LoanTerm": 36,
    "PreviousDefault": "No",
    "HomeOwnership": "Own"
}

applicant3 = {
    "Age": 32,
    "Income": 500000,
    "LoanAmount": 700000,
    "CreditScore": 620,
    "EmploymentYears": 4,
    "ExistingLoans": 3,
    "MonthlyDebt": 25000,
    "LoanTerm": 60,
    "PreviousDefault": "Yes",
    "HomeOwnership": "Rent"
}

applicant4 = {
    "Age": 40,
    "Income": 900000,
    "LoanAmount": 400000,
    "CreditScore": 750,
    "EmploymentYears": 12,
    "ExistingLoans": 1,
    "MonthlyDebt": 12000,
    "LoanTerm": 36,
    "PreviousDefault": "No",
    "HomeOwnership": "Mortgage"
}

applicant5 = {
    "Age": 29,
    "Income": 350000,
    "LoanAmount": 800000,
    "CreditScore": 590,
    "EmploymentYears": 2,
    "ExistingLoans": 5,
    "MonthlyDebt": 35000,
    "LoanTerm": 60,
    "PreviousDefault": "Yes",
    "HomeOwnership": "Rent"
}

print("\nApplicant 1:")
print(PredictLoanDefault(applicant1))

print("\nApplicant 2:")
print(PredictLoanDefault(applicant2))

print("\nApplicant 3:")
print(PredictLoanDefault(applicant3))

print("\nApplicant 4:")
print(PredictLoanDefault(applicant4))

print("\nApplicant 5:")
print(PredictLoanDefault(applicant5))

# ------------------------------------------------------------
# 23. HYPERPARAMETER EXPERIMENT 1
# ACTIVATION FUNCTION
# ------------------------------------------------------------

print("\n------------------------------------------------------------")
print("Experiment 1 - Activation Function")
print("------------------------------------------------------------")

activation_functions = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

activation_results = []

for activation in activation_functions:
    model_activation = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )
    
    model_activation.fit(X_train_scaled,y_train)

    prediction = model_activation.predict(X_test_scaled)

    accuracy = accuracy_score(y_test,prediction)

    activation_results.append([activation, accuracy])

activation_df = pd.DataFrame(
    activation_results,
    columns=[
        "Activation",
        "Accuracy"
    ]
)

print("\nActivation Experiment Results:")
print(activation_df)


# Plot activation results

plt.figure(figsize=(8, 5))
plt.bar(
    activation_df["Activation"],
    activation_df["Accuracy"]
)
plt.xlabel("Activation Function")
plt.ylabel("Testing Accuracy")

plt.title("Activation Function Comparison")
plt.show()

# ------------------------------------------------------------
# 24. Hyperparameter Experiment 2
# Hidden Layers
# ------------------------------------------------------------

print("\n------------------------------------------------------------")
print("Experiment 2 - Hidden Layers")
print("------------------------------------------------------------")

hidden_layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

hidden_results = []

for layers in hidden_layers:
    model_hidden = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model_hidden.fit(X_train_scaled,y_train)

    prediction = model_hidden.predict(X_test_scaled)

    accuracy = accuracy_score(y_test,prediction)

    hidden_results.append(
        [str(layers), accuracy]
    )

hidden_df = pd.DataFrame(
    hidden_results,
    columns=["Hidden Layers","Accuracy"]
)

print("\nHidden Layer Experiment Results:")
print(hidden_df)

# Plot hidden layer results

plt.figure(figsize=(8, 5))
plt.bar(
    hidden_df["Hidden Layers"],
    hidden_df["Accuracy"]
)
plt.xlabel("Hidden Layer Configuration")
plt.ylabel("Testing Accuracy")
plt.title("Hidden Layer Comparison")
plt.show()

# ------------------------------------------------------------
# 25. Hyperparameter Experiment 3
# Learning Rate
# ------------------------------------------------------------

print("\n------------------------------------------------------------")
print("Experiment 3 - Learning Rate")
print("------------------------------------------------------------")

learning_rates = [
    0.0001,
    0.001,
    0.01,
    0.1
]

learning_results = []

for rate in learning_rates:
    model_lr = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=rate,
        max_iter=1000,
        random_state=42
    )

    model_lr.fit(X_train_scaled,y_train)

    prediction = model_lr.predict(X_test_scaled)
    accuracy = accuracy_score(y_test,prediction)

    learning_results.append([rate, accuracy])

learning_df = pd.DataFrame(
    learning_results,
    columns=["Learning Rate","Accuracy"]
)

print("\nLearning Rate Experiment Results:")
print(learning_df)

# Plot learning rate results

plt.figure(figsize=(8, 5))
plt.plot(
    learning_df["Learning Rate"],
    learning_df["Accuracy"],
    marker="o"
)
plt.xlabel("Learning Rate")
plt.ylabel("Testing Accuracy")
plt.title("Learning Rate Comparison")
plt.grid()
plt.show()

# ------------------------------------------------------------
# 26. Find Best Hyperparameters
# ------------------------------------------------------------

print("\n------------------------------------------------------------")
print("Best Hyperparameters")
print("------------------------------------------------------------")

best_activation = activation_df.loc[activation_df["Accuracy"].idxmax()]

best_hidden = hidden_df.loc[hidden_df["Accuracy"].idxmax()]

best_learning_rate = learning_df.loc[learning_df["Accuracy"].idxmax()]

print("\nBest Activation:")
print(best_activation)

print("\nBest Hidden Layer:")
print(best_hidden)

print("\nBest Learning Rate:")
print(best_learning_rate)

# ------------------------------------------------------------
# 27. Overall Model Evaluation
# ------------------------------------------------------------
print("\n------------------------------------------------------------")
print("Overall Model Evaluation")
print("------------------------------------------------------------")

accuracy_difference = (train_accuracy - test_accuracy)

print("Training Accuracy : ",train_accuracy)
print("Testing Accuracy : ",test_accuracy)
print("Accuracy Difference : ",accuracy_difference)

if accuracy_difference > 0.10:
    print("\nConclusion: Model may be suffering from OVERFITTING.")
elif (train_accuracy < 0.70 and test_accuracy < 0.70):
    print("\nConclusion: Model may be suffering from UNDERFITTING.")
else:
    print("\nConclusion: Model has reasonable generalization.")

# ------------------------------------------------------------
# Final Summary
# ------------------------------------------------------------

print("\n------------------------------------------------------------")
print("Final Summary")
print("------------------------------------------------------------")
print("Training Accuracy : ",train_accuracy * 100,"%")
print("Testing Accuracy : ",test_accuracy * 100,"%")
print("Precision : ",precision)
print("Recall : ",recall)
print("F1 Score : ",f1)
print("Iterations : ",model.n_iter_)