# Breast Cancer Prediction

# Breast cancer is one of the leading causes of death among women worldwide. Early detection and accurate
# diagnosis play a critical role in increasing survival rates.

# You are given a dataset containing various medical features extracted from breast cancer biopsy images.
# Your task is to develop a machine learning model that can accurately predict whether a tumor is Malignant
# (harmful) or Benign (non-harmful) based on the given features.

# Dataset Details
#     Source: Breast Cancer Wisconsin Dataset
#     Number of Records: 569
#     Number of Features: 30 (real-valued features)

# Note : Use load_breast_cancer() method from sklearn to load the dataset.

# Features:
#     Mean Radius
#     Mean Texture
#     Mean Perimeter
#     Mean Area
#     Mean Smoothness
#     Mean Compactness
#     Mean Concavity
#     Mean Symmetry
#     Worst Radius, Worst Texture, ... (and other statistical measurements)

# Target Variable:
#     · 0 -> Malignant
#     · 1 -> Benign

# Objectives:

#     1. Load and explore the dataset.
#     2. Perform data preprocessing steps:
#         Handle missing values (if any)
#         Normalize or scale features
#     3. Perform exploratory data analysis (EDA):
#         Summary statistics
#         Visualization of feature correlations
#     4. Split the dataset into training and testing sets.
#     5. Build a machine learning classification model to predict tumor type.
#     6. Evaluate the model using:
#         Accuracy
#         Confusion Matrix
#         Precision, Recall, F1-Score
#     7. Provide your observations and conclusions.

# Expected Deliverables:

# Code File:
#     Data loading
#     Preprocessing
#     Model building
#     Evaluation

# Breast Cancer Prediction
# Using Logistic Regression

# ---------------------------------------------------
# 1. Import required libraries
# ---------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# ---------------------------------------------------
# 2. Load the dataset
# ---------------------------------------------------

data = load_breast_cancer()

# Convert features into DataFrame
X = pd.DataFrame(data.data, columns=data.feature_names)

# Target
Y = data.target

print("Dataset loaded successfully")


# ---------------------------------------------------
# 3. Explore the dataset
# ---------------------------------------------------

print("\nFirst 5 records:")
print(X.head())

print("\nDataset Shape:")
print(X.shape)

print("\nFeature Names:")
print(X.columns)

print("\nTarget Names:")
print(data.target_names)

print("\nTarget Values:")
print(Y[:10])


# ---------------------------------------------------
# 4. Check missing values
# ---------------------------------------------------

print("\nMissing Values:")
print(X.isnull().sum().sum())

if X.isnull().sum().sum() == 0:
    print("No missing values found.")


# ---------------------------------------------------
# 5. Summary Statistics
# ---------------------------------------------------

print("\nSummary Statistics:")
print(X.describe())


# ---------------------------------------------------
# 6. Check target distribution
# ---------------------------------------------------

print("\nTarget Distribution:")
print(pd.Series(Y).value_counts())

print("\nTarget Meaning:")
print("0 = Malignant")
print("1 = Benign")


# ---------------------------------------------------
# 7. Feature Correlation
# ---------------------------------------------------

plt.figure(figsize=(15, 10))

sns.heatmap(
    X.corr(),
    cmap="coolwarm",
    annot=False
)

plt.title("Feature Correlation Heatmap")
plt.show()


# ---------------------------------------------------
# 8. Split data into training and testing
# ---------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)


# ---------------------------------------------------
# 9. Feature Scaling
# ---------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ---------------------------------------------------
# 10. Create Logistic Regression model
# ---------------------------------------------------

model = LogisticRegression(max_iter=1000)


# ---------------------------------------------------
# 11. Train the model
# ---------------------------------------------------

model.fit(X_train_scaled, Y_train)

print("\nModel training completed.")


# ---------------------------------------------------
# 12. Make predictions
# ---------------------------------------------------

Y_pred = model.predict(X_test_scaled)


# ---------------------------------------------------
# 13. Calculate Accuracy
# ---------------------------------------------------

accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy:")
print("{:.2f}%".format(accuracy * 100))


# ---------------------------------------------------
# 14. Confusion Matrix
# ---------------------------------------------------

cm = confusion_matrix(Y_test, Y_pred)

print("\nConfusion Matrix:")
print(cm)


# ---------------------------------------------------
# 15. Plot Confusion Matrix
# ---------------------------------------------------

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Malignant", "Benign"],
    yticklabels=["Malignant", "Benign"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# ---------------------------------------------------
# 16. Classification Report
# ---------------------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        Y_test,
        Y_pred,
        target_names=["Malignant", "Benign"]
    )
)