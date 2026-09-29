# 2: Write a Python program to demonstrate ReLU and Max Pooling.

# Tasks:
#     1. Create a feature map with positive and negative values.
#     2. Apply ReLU.
#     3. Apply 2x2 max pooling.
#     4. Display output after each step.
#     5. Explain why pooling reduces size.

# Input Feature Map:

# feature_map =[
# [3,3,3],
# [0,0,0],
# [-3, -3, -3]
# ]

# ReLU Rule:
# If value < 0, convert it to 0
# If value >= 0, keep it same

# Expected Output:

# relu_output = [
#     [3,3,3],
#     [0,0,0],
#     [0,0,0]
# ]

# 2: Write a Python program to demonstrate ReLU and Max Pooling.

# Tasks:
# 1. Create a feature map with positive and negative values.
# 2. Apply ReLU.
# 3. Apply 2x2 max pooling.
# 4. Display output after each step.
# 5. Explain why pooling reduces size.


# ------------------------------------------------------------
# Step 1: Create Feature Map
# ------------------------------------------------------------

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

print("Original Feature Map:")
for row in feature_map:
    print(row)


# ------------------------------------------------------------
# Step 2: Apply ReLU
#
# ReLU Rule:
# If value < 0, convert it to 0
# If value >= 0, keep it same
# ------------------------------------------------------------

relu_output = []

for row in feature_map:

    relu_row = []

    for value in row:

        if value < 0:
            relu_row.append(0)
        else:
            relu_row.append(value)

    relu_output.append(relu_row)


print("\nReLU Output:")
for row in relu_output:
    print(row)


# ------------------------------------------------------------
# Expected ReLU Output:
#
# [3, 3, 3]
# [0, 0, 0]
# [0, 0, 0]
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 3: Apply 2x2 Max Pooling
# ------------------------------------------------------------

pool_size = 2

rows = len(relu_output)
cols = len(relu_output[0])

# Calculate output size
# Formula:
# Output Size = Input Size - Pool Size + 1

output_rows = rows - pool_size + 1
output_cols = cols - pool_size + 1

pooling_output = []


for i in range(output_rows):

    pooling_row = []

    for j in range(output_cols):

        # Create 2x2 region

        value1 = relu_output[i][j]
        value2 = relu_output[i][j + 1]
        value3 = relu_output[i + 1][j]
        value4 = relu_output[i + 1][j + 1]

        # Store values in a list

        region = [
            value1,
            value2,
            value3,
            value4
        ]

        print("\n2x2 Region:")
        print(value1, value2)
        print(value3, value4)

        # Find maximum value

        maximum = max(region)

        print("Maximum Value:", maximum)

        # Add maximum value to output

        pooling_row.append(maximum)

    pooling_output.append(pooling_row)


# ------------------------------------------------------------
# Step 4: Display Max Pooling Output
# ------------------------------------------------------------

print("\nMax Pooling Output:")

for row in pooling_output:
    print(row)


# ------------------------------------------------------------
# Step 5: Explain Size Reduction
# ------------------------------------------------------------

print("\nWhy does pooling reduce size?")

print("Max Pooling takes a 2x2 region")
print("and selects only the maximum value.")
print("Therefore, multiple values are represented by one value.")
print("This reduces the size of the feature map.")