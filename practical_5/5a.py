import numpy as np

# Step 1: Define binary patterns (+1/-1)
patterns = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])

# Step 2: Initialize weight matrix
n = patterns.shape[1]
W = np.zeros((n, n))

# Step 3: Hebbian learning rule
for p in patterns:
    W += np.outer(p, p)

W[np.diag_indices(n)] = 0  # No self-connections

# Step 4: Define recall function
def recall(x, W, steps=5):
    for _ in range(steps):
        x = np.sign(W @ x)
        x[x == 0] = 1   # avoid zero states
    return x

# Step 5: Test with noisy input
test = np.array([1, -1, -1, -1])
output = recall(test, W)

print("Recalled pattern:", output)

