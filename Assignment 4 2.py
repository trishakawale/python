import numpy as np

print("Enter elements for 5x3 matrix:")
matrix1 = []

for i in range(5):
    row = list(map(int, input(f"Enter row {i+1} (3 elements): ").split()))
    matrix1.append(row)

print("\nEnter elements for 3x2 matrix:")
matrix2 = []

for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (2 elements): ").split()))
    matrix2.append(row)

# Convert lists to NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Matrix multiplication
product = np.dot(matrix1, matrix2)

print("\nProduct Matrix (5x2):")
print(product)
