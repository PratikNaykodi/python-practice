# 3. Write a Python program to calculate loss manually.

# Tasks:
# 1. Implement Mean Squared Error.
# 2. Implement Binary Cross Entropy.
# 3. Take actual and predicted values.
# 4. Display the calculated loss.
# 5. Explain which loss function is used for regression and classification.
# Ans: Mean Squared Error(MSE) is commonly used for regression because it measures the difference between continuous actual and predicted values. Binary Cross Entropy is commonly used for binary classification because it measures how close the predicted probability is to the actual class (0 or 1).

import math

# Actual values
actual = [1, 0, 1, 1]

# Predicted values
predicted = [0.9, 0.2, 0.8, 0.7]


# --------------------------------------------------------------
# 1. Mean Squared Error
# --------------------------------------------------------------

def mean_squared_error(actual, predicted):
    total = 0

    for i in range(len(actual)):
        error = actual[i] - predicted[i]
        total = total + (error ** 2)

    mse = total / len(actual)

    return mse


# --------------------------------------------------------------
# 2. Binary Cross Entropy
# --------------------------------------------------------------

def binary_cross_entropy(actual, predicted):
    total = 0

    for i in range(len(actual)):
        loss = (
            actual[i] * math.log(predicted[i])
            + (1 - actual[i]) * math.log(1 - predicted[i])
        )

        total = total + loss

    bce = -total / len(actual)

    return bce


# Calculate losses
mse = mean_squared_error(actual, predicted)
bce = binary_cross_entropy(actual, predicted)


# Display results
print("Actual Values   :", actual)
print("Predicted Values:", predicted)

print("\nMean Squared Error:", mse)
print("Binary Cross Entropy:", bce)