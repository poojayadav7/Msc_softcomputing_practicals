import numpy as np
import matplotlib.pyplot as plt

# Function to create a distance calculator for a line ax + by + c = 0
def create_distance_function(a, b, c):
    def distance(x, y):
        nom = a * x + b * y + c
        pos = 0 if nom == 0 else (-1 if (nom < 0 and b < 0) or (nom > 0 and b > 0) else 1)
        d = abs(nom) / np.sqrt(a**2 + b**2)
        return d, pos
    return distance


# --- Main Program ---
points = [(3.5, 1.8), (1.1, 3.9)]  # Two sample points

fig, ax = plt.subplots()
ax.set(xlabel="sweetness", ylabel="sourness", xlim=[-1, 6], ylim=[-1, 8])

X = np.arange(-0.5, 5, 0.1)

# Plot sample points
ax.plot(points[0][0], points[0][1], 'o', color='darkorange', markersize=10)
ax.plot(points[1][0], points[1][1], 'oy', markersize=10)

# Test all possible separating lines
for x in np.arange(0, 1.05, 0.05):
    slope = np.tan(np.arccos(x))
    dist_func = create_distance_function(slope, -1, 0)
    Y = slope * X
    results = [dist_func(*p) for p in points]
    color = 'g-' if results[0][1] != results[1][1] else 'r-'
    ax.plot(X, Y, color)

plt.title("Line Separation based on Distance Function")
plt.show()

