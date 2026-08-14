# These data are the results of a chemical analysis of wines grown in the same region in Italy
# but derived from three different cultivars. The analysis determined the quantities of 13
# constituents found in each of the three types of wines.

# Wine data set contains 13 features as

# 1) Alcohol
# 2) Malic acid
# 3) Ash
# 4) Alcalinity of ash
# 5) Magnesium
# 6) Total phenols
# 7) Flavanoids
# 8) Nonflavanoid phenols
# 9) Proanthocyanins
# 10)Color intensity
# 11)Hue
# 12)OD280/OD315 of diluted wines
# 13)Proline

# According to the above features wine can be classified as
# . Class 1
# . Class 2
# . Class 3

# Design machine learning application which follows below steps as

# Step 1:
# Get Data

# Step 2:
# Clean, Prepare and Manipulate data

# Step 3:
# Train Data

# Step 4:
# Test Data

# Step 5:
# Calculate Accuracy

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ==========================================================
# Step 1: Get Data
# ==========================================================

df = pd.read_csv("WinePredictor.csv")

print("First 5 records:")
print(df.head())

print("\nDataset Information:")
print(df.info())


# ==========================================================
# Step 2: Clean, Prepare and Manipulate Data
# ==========================================================

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

# Separate features and target
X = df.drop("Class", axis=1)
Y = df["Class"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(Y.head())


# ==========================================================
# Step 3: Train Data
# ==========================================================

# Split data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)

print("\nTraining data size:", X_train.shape)
print("Testing data size:", X_test.shape)


# Scale the features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Create Machine Learning model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train_scaled, Y_train)


# ==========================================================
# Step 4: Test Data
# ==========================================================
Y_pred = model.predict(X_test_scaled)

print("\nActual Values:")
print(Y_test.values)

print("\nPredicted Values:")
print(Y_pred)

# ==========================================================
# Step 5: Calculate Accuracy
# ==========================================================
accuracy = accuracy_score(Y_test, Y_pred)

print("\n======================================")
print("Wine Classification Result")
print("======================================")

print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))