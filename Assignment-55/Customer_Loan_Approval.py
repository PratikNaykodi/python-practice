# Customer Loan Approval Using Voting Classification

# A bank wants to automate its loan approval process.

# The bank has historical information about customers such as:
#     Age
#     Income
#     Credit Score
#     Existing Loan
#     Employment Experience
#     Loan Amount


# The target column is:
# LoanApproved

# where:
# 0 - Loan Rejected
# 1 -Loan Approved
# The bank does not want to depend on a single Machine Learning algorithm.

# Build a Voting Classifier using:
#     Logistic Regression
#     Decision Tree
#     K-Nearest Neighbors

# Tasks:
#     1. Load the dataset.
#     2. Check for missing values.
#     3. Separate input and output variables.
#     4. Split the dataset into training and testing data.
#     5. Train Logistic Regression.
#     6. Train Decision Tree.
#     7. Train KNN.
#     8. Calculate the individual accuracy of all three algorithms.
#     9. Create a Hard Voting Classifier.
#     10. Calculate its accuracy.
#     11. Create a Soft Voting Classifier.
#     12. Calculate its accuracy.
#     13. Compare:

# Model                      Accuracy
# Logistic Regression
# Decision Tree
# KNN
# Hard Voting
# Soft Voting

# Customer Loan Approval Using Voting Classification

# --------------------------------------------------
# 1. Import Libraries
# --------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score


# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

df = pd.read_csv("Customer_Loan_Approval.csv")

print("First 5 records:")
print(df.head())


# --------------------------------------------------
# 3. Check Dataset Information
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 4. Separate Input and Output Variables
# --------------------------------------------------

X = df.drop("LoanApproved", axis=1)

Y = df["LoanApproved"]


# --------------------------------------------------
# 5. Split Dataset into Training and Testing
# --------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)


# --------------------------------------------------
# 6. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 7. Create Individual Models
# --------------------------------------------------

logistic_model = LogisticRegression(
    max_iter=1000
)

decision_tree_model = DecisionTreeClassifier(
    random_state=42
)

knn_model = KNeighborsClassifier(
    n_neighbors=5
)


# --------------------------------------------------
# 8. Train Logistic Regression
# --------------------------------------------------

logistic_model.fit(
    X_train_scaled,
    Y_train
)

logistic_pred = logistic_model.predict(
    X_test_scaled
)

logistic_accuracy = accuracy_score(
    Y_test,
    logistic_pred
)


# --------------------------------------------------
# 9. Train Decision Tree
# --------------------------------------------------

decision_tree_model.fit(
    X_train,
    Y_train
)

decision_tree_pred = decision_tree_model.predict(
    X_test
)

decision_tree_accuracy = accuracy_score(
    Y_test,
    decision_tree_pred
)


# --------------------------------------------------
# 10. Train KNN
# --------------------------------------------------

knn_model.fit(
    X_train_scaled,
    Y_train
)

knn_pred = knn_model.predict(
    X_test_scaled
)

knn_accuracy = accuracy_score(
    Y_test,
    knn_pred
)


# --------------------------------------------------
# 11. Create Hard Voting Classifier
# --------------------------------------------------

hard_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="hard"
)


# Train Hard Voting
hard_voting.fit(
    X_train_scaled,
    Y_train
)

hard_pred = hard_voting.predict(
    X_test_scaled
)

hard_accuracy = accuracy_score(
    Y_test,
    hard_pred
)


# --------------------------------------------------
# 12. Create Soft Voting Classifier
# --------------------------------------------------

soft_voting = VotingClassifier(
    estimators=[
        ("lr", LogisticRegression(max_iter=1000)),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="soft"
)


# Train Soft Voting
soft_voting.fit(
    X_train_scaled,
    Y_train
)

soft_pred = soft_voting.predict(
    X_test_scaled
)

soft_accuracy = accuracy_score(
    Y_test,
    soft_pred
)


# --------------------------------------------------
# 13. Display Individual Model Accuracy
# --------------------------------------------------

print("\n")
print("=" * 50)
print("INDIVIDUAL MODEL ACCURACY")
print("=" * 50)

print(
    "Logistic Regression : {:.2f}%".format(
        logistic_accuracy * 100
    )
)

print(
    "Decision Tree       : {:.2f}%".format(
        decision_tree_accuracy * 100
    )
)

print(
    "KNN                 : {:.2f}%".format(
        knn_accuracy * 100
    )
)


# --------------------------------------------------
# 14. Display Voting Accuracy
# --------------------------------------------------

print("\n")
print("=" * 50)
print("VOTING CLASSIFIER ACCURACY")
print("=" * 50)

print(
    "Hard Voting : {:.2f}%".format(
        hard_accuracy * 100
    )
)

print(
    "Soft Voting : {:.2f}%".format(
        soft_accuracy * 100
    )
)


# --------------------------------------------------
# 15. Final Comparison
# --------------------------------------------------

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],

    "Accuracy": [
        logistic_accuracy * 100,
        decision_tree_accuracy * 100,
        knn_accuracy * 100,
        hard_accuracy * 100,
        soft_accuracy * 100
    ]
})


print("\n")
print("=" * 50)
print("FINAL MODEL COMPARISON")
print("=" * 50)

print(comparison.round(2))