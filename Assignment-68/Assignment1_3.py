# 3: Write a Python program to show flattening.

# Tasks:
#     1. Take a 2D matrix.
#     2. Convert it into a 1D vector.
#     3. Pass it to a fully connected layer.
#     4. Calculate final output manually.
#     5. Explain the role of flatten layer in CNN.

# Input Matrix:

# matrix = [
#     [6,4],
#     [8,6]
# ]

# Expected Flatten Output:
# flatten_output = [6,4, 8, 6]

# ------------------------------------------------------------
# Step 1: Input 2D Matrix
# ------------------------------------------------------------

matrix = [
    [6, 4],
    [8, 6]
]

print("Original 2D Matrix:")

for row in matrix:
    print(row)


# ------------------------------------------------------------
# Step 2: Flatten the Matrix
#
# Convert:
#
# [6, 4]
# [8, 6]
#
# Into:
#
# [6, 4, 8, 6]
# ------------------------------------------------------------

flatten_output = []

for row in matrix:

    for value in row:

        flatten_output.append(value)


print("\nFlatten Output:")
print(flatten_output)


# ------------------------------------------------------------
# Step 3: Fully Connected Layer
#
# We have 4 input values:
#
# 6, 4, 8, 6
#
# Let's define weights and bias.
# ------------------------------------------------------------

weights = [0.1, 0.2, 0.3, 0.4]

bias = 1


# ------------------------------------------------------------
# Step 4: Calculate Fully Connected Output
#
# Formula:
#
# Output = (Input1 * Weight1)
#        + (Input2 * Weight2)
#        + (Input3 * Weight3)
#        + (Input4 * Weight4)
#        + Bias
# ------------------------------------------------------------

total = 0

print("\nFully Connected Calculation:")

for i in range(len(flatten_output)):

    multiplication = flatten_output[i] * weights[i]

    print(
        flatten_output[i],
        "*",
        weights[i],
        "=",
        multiplication
    )

    total = total + multiplication


# Add bias

total = total + bias


print("\nBias =", bias)

print("\nFinal Output:")
print(total)


# ------------------------------------------------------------
# Step 5: Explain Flattening
# ------------------------------------------------------------

print("\nExplanation:")

print("Flattening converts a 2D or 3D feature map into a 1D vector.")

print("The Flatten layer connects the CNN feature extraction")
print("part with the Fully Connected layer.")

print("The Fully Connected layer uses the flattened values")
print("to calculate the final prediction.")
