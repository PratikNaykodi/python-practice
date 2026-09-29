# 1: Write a Python program to manually perform convolution.

# Input:
# A 5x5 matrix representing grayscale image.

# Kernel:
# A 3x3 edge detection filter.

# Tasks:
#     1. Move kernel over image.
#     2. Perform multiplication and addition.
#     3. Generate feature map.
#     4. Print each region calculation.

# Input Image Matrix

# image = [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [1,1,1,1,1],
#     [0,0,0,0,0],
#     [0,0,0,0,0]
# ]

# Kernel Matrix:

# kernel = [
#     [-1,-1,-1],
#     [ 0,0,0],
#     [ 1,1,1]
# ]

# First Region Calculation:

# Region:
# 0 0 0
# 0 0 0
# 1 1 1

# Kernel:
# -1 -1 -1
# 0  0  0  
# 1  1  1

# Calculation:
# 0 *- 1 + 0 *- 1 + 0 *- 1 + 0 * 0 + 0 * 0 + 0 * 0 + 1 * 1 + 1 * 1 + 1 * 1

# Output = 3

# Expected Feature Map:
# feature_map = [
# [3,3,3],
# [0,0,0],
# [-3, -3, -3]
# ]


# ------------------------------------------------------------
# Input Image Matrix
# ------------------------------------------------------------

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# ------------------------------------------------------------
# 3x3 Kernel Matrix
# Edge Detection Filter
# ------------------------------------------------------------

kernel = [
    [-1, -1, -1],
    [0,  0,  0],
    [1,  1,  1]
]

# ------------------------------------------------------------
# Get Image and Kernel Size
# ------------------------------------------------------------

image_rows = len(image)
image_cols = len(image[0])

kernel_rows = len(kernel)
kernel_cols = len(kernel[0])

# ------------------------------------------------------------
# Feature Map Size
#
# Formula:
# Output Size = Input Size - Kernel Size + 1
#
# 5 - 3 + 1 = 3
# ------------------------------------------------------------

feature_rows = image_rows - kernel_rows + 1
feature_cols = image_cols - kernel_cols + 1

feature_map = []

# ------------------------------------------------------------
# Perform Convolution
# ------------------------------------------------------------

for i in range(feature_rows):

    feature_row = []

    for j in range(feature_cols):

        total = 0

        print("\n----------------------------------------")
        print("Region Calculation")
        print("----------------------------------------")

        print("Region:")

        # Print current 3x3 region
        for ki in range(kernel_rows):

            region_row = []

            for kj in range(kernel_cols):

                value = image[i + ki][j + kj]
                region_row.append(value)

            print(region_row)

        print("\nKernel:")

        for row in kernel:
            print(row)

        print("\nCalculation:")

        # Perform multiplication and addition
        for ki in range(kernel_rows):

            for kj in range(kernel_cols):

                image_value = image[i + ki][j + kj]
                kernel_value = kernel[ki][kj]

                multiplication = image_value * kernel_value

                print(
                    f"{image_value} * {kernel_value} = {multiplication}"
                )

                total = total + multiplication

        print("\nOutput =", total)

        feature_row.append(total)

    feature_map.append(feature_row)

# ------------------------------------------------------------
# Print Final Feature Map
# ------------------------------------------------------------

print("\n========================================")
print("Final Feature Map")
print("========================================")

for row in feature_map:
    print(row)