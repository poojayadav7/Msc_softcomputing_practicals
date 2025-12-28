import math

# Number of elements as input
n = int(input("Enter number of elements: "))

# Input values
print("Enter the inputs:")
inputs = []
for i in range(n):
    inputs.append(float(input(f"Input {i+1}: ")))

# Weight values
print("Enter the weights:")
weights = []
for i in range(n):
    weights.append(float(input(f"Weight {i+1}: ")))

# Calculate Yin
Yin = 0
for i in range(n):
    Yin += inputs[i] * weights[i]

print("Net Input (Yin) =", round(Yin, 3))

# Binary Sigmoid
binary_sigmoid = 1 / (1 + math.exp(-Yin))
print("Binary Sigmoid Output =", round(binary_sigmoid, 3))

# Bipolar Sigmoid
bipolar_sigmoid = (2 / (1 + math.exp(-Yin))) - 1
print("Bipolar Sigmoid Output =", round(bipolar_sigmoid, 3))
