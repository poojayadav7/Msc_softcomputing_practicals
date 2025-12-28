import numpy as np
import matplotlib.pyplot as plt

class RBF:
    def __init__(self, indim, numCenters, outdim):
        self.numCenters, self.beta = numCenters, 8
        self.centers = [np.random.uniform(-1, 1, indim) for _ in range(numCenters)]
        self.W = np.random.random((numCenters, outdim))  # weights

    def _basis(self, c, x):  # Gaussian basis function
        return np.exp(-self.beta * np.linalg.norm(c - x) ** 2)

    def _G(self, X):  # Activation matrix
        return np.array([[self._basis(c, x) for c in self.centers] for x in X])

    def train(self, X, Y):
        self.centers = [X[i] for i in np.random.choice(len(X), self.numCenters, replace=False)]  # pick centers
        G = self._G(X)                         # compute activations
        self.W = np.linalg.pinv(G) @ Y         # compute weights (least squares)

    def predict(self, X):
        return self._G(X) @ self.W             # output prediction


# ----- MAIN -----
x = np.linspace(-1, 1, 100).reshape(-1, 1)
y = np.sin(3 * (x + 0.5)**3 - 1)

rbf = RBF(1, 10, 1)
rbf.train(x, y)
z = rbf.predict(x)

# Plot results
plt.plot(x, y, 'k-', label='Original')
plt.plot(x, z, 'r--', label='RBF Approx')
plt.scatter([c[0] for c in rbf.centers], np.zeros(rbf.numCenters), color='g', label='Centers')
plt.legend(); plt.title('RBF Network Approximation')
plt.show()
