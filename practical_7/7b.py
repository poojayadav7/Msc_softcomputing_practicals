import numpy as np
import matplotlib.pyplot as plt

def show(p, title=""):
    plt.imshow(p.reshape(5,5), cmap="gray"); plt.title(title); plt.show()

# Create 5×5 checkerboard (size = 25)
checker = np.array([1,-1]*3 + [-1,1]*3 + [1,-1]*3 + [-1,1]*3 + [1,-1]*3)[:25]

# Make noisy version by flipping 4 bits
noisy = checker.copy()
noisy[np.random.choice(25, 4, replace=False)] *= -1

# Train Hopfield (Hebbian rule)
W = np.outer(checker, checker)
np.fill_diagonal(W, 0)

# Recall (run for few steps)
state = noisy.copy()
for _ in range(4):
    state = np.sign(W @ state)

# Show results
show(checker, "Original")
show(noisy, "Noisy")
show(state, "Recovered")
