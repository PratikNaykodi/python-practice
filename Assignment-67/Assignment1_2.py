# 2 : Create a neural network model to predict loan approval.

# Features:
# 1. Applicant income
# 2. Credit score
# 3. Loan amount
# 4. Existing EMI
# 5. Employment status

# Output:
# 0 = Loan rejected
# 1 = Loan approved

# Tasks:
#     1. Preprocess categorical values.
#     2. Apply scaling.
#     3. Train FNN model.
#     4. Evaluate model.
#     5. Predict approval for new applicant.

# Dataset
# X = [
#     [25000, 600, 200000, 10000, 0],
#     [40000, 700, 300000, 8000, 1],
#     [60000, 750, 500000, 12000, 1],
#     [20000, 550, 150000, 15000, 0],
#     [80000, 800, 700000, 10000, 1],
#     [35000, 650, 250000, 9000, 1],
#     [18000, 500, 100000, 12000, 0],
#     [90000, 850, 800000, 15000, 1],
#     [30000, 580, 200000, 14000, 0],
#     [70000, 780, 600000, 10000, 1]
# ]

# y = [
#     0, 1, 1, 0, 1,
#     1, 0, 1, 0, 1
# ]

# Feature Meaning:

# [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]

# Employment Status:
# 0 = Not Stable
# 1 = Stable

# Test Input:
# new_applicant = [[55000, 720, 400000, 10000, 1]]

# Expected Output:
# Prediction: Loan Approved

# --------------------------------------------------------------
# Loan Approval Prediction using FNN
#
# Features:
# 1. Applicant Income
# 2. Credit Score
# 3. Loan Amount
# 4. Existing EMI
# 5. Employment Status
#
# Output:
# 0 = Loan Rejected
# 1 = Loan Approved
# --------------------------------------------------------------

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# --------------------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------------------
X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
])

# --------------------------------------------------------------
# 2. Check Dataset
# --------------------------------------------------------------
print("Dataset Shape:", X.shape)

print("Missing Values:", np.isnan(X).sum())

# --------------------------------------------------------------
# 3. Preprocess Categorical Value
# --------------------------------------------------------------

# Employment Status:
# 0 = Not Stable
# 1 = Stable
#
# It is already encoded numerically,
# so no additional encoding is required.

# --------------------------------------------------------------
# 4. Split Dataset
# --------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------------------
# 5. Apply StandardScaler
# --------------------------------------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# --------------------------------------------------------------
# 6. Create FNN Model
# --------------------------------------------------------------
model = Sequential()

# Input Layer + First Hidden Layer
model.add(Dense(
    10,
    activation="relu",
    input_shape=(5,)
))

# Second Hidden Layer
model.add(Dense(
    5,
    activation="relu"
))

# Output Layer
model.add(Dense(
    1,
    activation="sigmoid"
))

# --------------------------------------------------------------
# 7. Compile Model
# --------------------------------------------------------------
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# --------------------------------------------------------------
# 8. Train Model
# --------------------------------------------------------------
model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)

# --------------------------------------------------------------
# 9. Evaluate Model
# --------------------------------------------------------------
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)

# --------------------------------------------------------------
# 10. Predict New Applicant
# --------------------------------------------------------------
new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

# Apply the same scaler
new_applicant_scaled = scaler.transform(new_applicant)

# Predict probability
prediction_probability = model.predict(
    new_applicant_scaled,
    verbose=0
)

probability = prediction_probability[0][0]

print("\nApproval Probability:", probability)

# --------------------------------------------------------------
# 11. Convert Probability into Class
# --------------------------------------------------------------

if probability >= 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")