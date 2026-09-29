# 2. Write a Python program to demonstrate different activation functions.
# Functions to implement:
# 1. Sigmoid
# 2. ReLU
# 3. Tanh

# Tasks:
# 1. Accept input values from -10 to 10.
# 2. Plot all activation functions using Matplotlib.
# 3. Explain the use of each activation function.

# --------------------------------------------------------------
# Program: Demonstrate Different Activation Functions
# Functions:
# 1. Sigmoid
# 2. ReLU
# 3. Tanh
# --------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create input values from -10 to 10
x = np.linspace(-10, 10, 100)

# Step 2: Define Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Step 3: Define ReLU function
def relu(x):
    return np.maximum(0, x)

# Step 4: Define Tanh function
def tanh(x):
    return np.tanh(x)

# Step 5: Calculate output for each activation function
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

# Step 6: Plot all activation functions
plt.plot(x, sigmoid_output, label="Sigmoid")
plt.plot(x, relu_output, label="ReLU")
plt.plot(x, tanh_output, label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")

plt.grid(True)
plt.legend()
plt.show()

# 1. Sigmoid

# Formula:
#     Sigmoid(x)=1/1+e^-x 
# Output range: 0 to 1
# Commonly used in the output layer for binary classification.
# Example: predicting Yes/No, Pass/Fail, 0/1.

# 2. ReLU

# Formula:
# ReLU(x)=max(0,x)
# Negative values become 0.
# Positive values remain unchanged.
# Commonly used in hidden layers of neural networks.
# It is simple and computationally fast.

# Example:
# Input: -5  →  0
# Input:  0  →  0
# Input:  5  →  5

# 3. Tanh

# Formula:
# Tanh(x)=e^x-e^-x/e^x+e^-x
# Output range: -1 to 1
# Similar to sigmoid but centered around 0.
# Historically/common in some neural-network architectures, especially recurrent networks.

# Example:
# Input: -10  → approximately -1
# Input:   0  → 0
# Input:  10  → approximately 1