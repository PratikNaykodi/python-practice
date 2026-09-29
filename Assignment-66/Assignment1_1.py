# 1: Write a Python program to simulate a single artificial neuron.

# Input:
# x1 = 2
# x2 = 3
# w1 = 0.4
# w2 = 0.6
# bias = 0.5

# Tasks:

# 1. Calculate weighted sum.
# 2. Apply sigmoid activation function.
# 3. Display final output.
# 4. Explain whether output is close to 0 or 1.

import math

# Input values
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# Step 1: Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias

print("Weighted Sum:", weighted_sum)

# Step 2: Apply Sigmoid Activation Function
sigmoid = 1 / (1 + math.exp(-weighted_sum))
print("Sigmoid Output:", sigmoid)

# Step 3: Display final output
print("Final Output:", sigmoid)

# Step 4: Explain output
if sigmoid >= 0.5:
    print("Output is close to 1.")
else:
    print("Output is close to 0.")

# Output:
# Weighted Sum: 3.0999999999999996
# Sigmoid Output: 0.9568927450589139
# Final Output: 0.9568927450589139
# Output is close to 1.