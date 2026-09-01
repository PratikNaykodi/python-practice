# Fraudulent Transaction Detection

# A financial institution wants to detect potentially fraudulent transactions.

# Available information includes:

#     Transaction Amount
#     Transaction Time
#     Account Age
#     Number of Previous Transactions
#     Location Difference
#     Device Type
#     Failed Login Attempts

# Target:
# Fraud
# 0 -> Normal Transaction
# 1 -> Fraudulent Transaction
# You must investigate different ensemble approaches and recommend the most suitable model.

# Tasks
# Build and compare:
#     1. Decision Tree
#     2. Bagging Classifier
#     3. Random Forest Classifier
#     4. AdaBoost Classifier
#     5. Voting Classifier

# Evaluate each model using:
#     Accuracy
#     Precision
#     Recall
#     F1 Score
#     Confusion Matrix

# Prepare a final comparison:

# Algorithm         Accuracy      Precision   Recall   F1
# Decision Tree
# Bagging
# Random Forest
# AdaBoost
# Voting

# Fraudulent Transaction Detection
# Comparing Ensemble Learning Algorithms

# ---------------------------------------------------
# 1. Import required libraries
# ---------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ---------------------------------------------------
# 2. Load Dataset
# ---------------------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("First 5 records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())


# ---------------------------------------------------
# 3. Separate Features and Target
# ---------------------------------------------------

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]


# ---------------------------------------------------
# 4. Define numerical and categorical features
# ---------------------------------------------------

numerical_features = [
    "TransactionAmount",
    "TransactionHour",
    "AccountAgeMonths",
    "PreviousTransactions",
    "LocationDifferenceKm",
    "FailedLoginAttempts"
]

# Categorical feature
categorical_features = [
    "DeviceType"
]


# ---------------------------------------------------
# 5. Preprocessing
# ---------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# ---------------------------------------------------
# 6. Train-Test Split
# ---------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)


# ---------------------------------------------------
# 7. Transform the data
# ---------------------------------------------------

X_train_processed = preprocessor.fit_transform(X_train)

X_test_processed = preprocessor.transform(X_test)


# ---------------------------------------------------
# 8. Create Models
# ---------------------------------------------------

decision_tree = DecisionTreeClassifier(
    random_state=42
)

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=100,
    random_state=42
)

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

adaboost = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)


# Voting Classifier
logistic = LogisticRegression(
    max_iter=1000
)

voting = VotingClassifier(
    estimators=[
        ("lr", logistic),
        ("dt", DecisionTreeClassifier(random_state=42)),
        ("rf", RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ))
    ],
    voting="soft"
)


# ---------------------------------------------------
# 9. Store all models
# ---------------------------------------------------

models = {
    "Decision Tree": decision_tree,
    "Bagging": bagging,
    "Random Forest": random_forest,
    "AdaBoost": adaboost,
    "Voting": voting
}


# ---------------------------------------------------
# 10. Train and Evaluate Models
# ---------------------------------------------------

results = []

for name, model in models.items():

    # Train model
    model.fit(X_train_processed, Y_train)

    # Predict
    Y_pred = model.predict(X_test_processed)

    # Calculate metrics
    accuracy = accuracy_score(Y_test, Y_pred)

    precision = precision_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    recall = recall_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    f1 = f1_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    # Confusion Matrix
    cm = confusion_matrix(
        Y_test,
        Y_pred
    )

    # Store results
    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    # Display individual results
    print("\n")
    print("=" * 50)
    print(name)
    print("=" * 50)

    print("Accuracy  :", round(accuracy, 4))
    print("Precision :", round(precision, 4))
    print("Recall    :", round(recall, 4))
    print("F1 Score  :", round(f1, 4))

    print("\nConfusion Matrix:")
    print(cm)


# ---------------------------------------------------
# 11. Create Final Comparison Table
# ---------------------------------------------------

results_df = pd.DataFrame(
    results,
    columns=[
        "Algorithm",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print("\n")
print("=" * 70)
print("FINAL MODEL COMPARISON")
print("=" * 70)

print(results_df)


# ---------------------------------------------------
# 12. Convert metrics to percentage
# ---------------------------------------------------

results_percentage = results_df.copy()

results_percentage[
    ["Accuracy", "Precision", "Recall", "F1"]
] = results_percentage[
    ["Accuracy", "Precision", "Recall", "F1"]
] * 100

print("\nComparison in Percentage:")
print(results_percentage.round(2))


# ---------------------------------------------------
# 13. Find the best model
# ---------------------------------------------------

best_model = results_df.loc[
    results_df["F1"].idxmax()
]

print("\nBest Model based on F1 Score:")
print(best_model["Algorithm"])

print("\nBest F1 Score:")
print(round(best_model["F1"], 4))