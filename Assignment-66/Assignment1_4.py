# 4. Write a Python program to show how weights are updated in ANN.
# Tasks:
# 1. Take input, weight, bias, target output, and learning rate.
# 2. Calculate prediction.
# 3. Calculate error.
# 4. Update weight using gradient descent logic.
# 5. Display old weight and updated weight.


# Get input values from user
x = float(input("Enter input (x): "))
weight = float(input("Enter initial weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

# Step 1: Calculate prediction
prediction = (x * weight) + bias
print("\nPrediction:", prediction)

# Step 2: Calculate error
error = target - prediction
print("Error:", error)


# Step 3: Calculate gradient
gradient = error * x
print("Gradient:", gradient)

# Step 4: Store old weight
old_weight = weight

# Step 5: Update weight
weight = weight + (learning_rate * gradient)

# Step 6: Display result
print("\nOld Weight:", old_weight)
print("Updated Weight:", weight)