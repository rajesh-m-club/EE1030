import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 9e9  # Coulomb's constant (N·m²/C²)

# Charge positions and values
charges = [
    (+1, (0, 1)),   # q1 at (0,1)
    (+1, (0, -1)),  # q2 at (0,-1)
    (-1, (1, 0)),   # q3 at (1,0)
    (-1, (-1, 0))   # q4 at (-1,0)
]

# Grid for plotting
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Initialize electric field components
Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)

# Compute Electric Field at each point
for q, (qx, qy) in charges:
    rx, ry = X - qx, Y - qy  # Displacement vector components
    r = np.sqrt(rx**2 + ry**2)  # Distance
    r[r == 0] = 1e-9  # Prevent division by zero
    Ex += k * q * rx / r**3
    Ey += k * q * ry / r**3

# Normalize vectors for quiver plot
magnitude = np.sqrt(Ex**2 + Ey**2)
Ex, Ey = Ex / magnitude, Ey / magnitude  # Normalize for visualization

# Plotting
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, Ex, Ey, color='r', scale=20)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Electric Field Vector Plot")
plt.scatter(*zip(*[pos for _, pos in charges]), color=['blue', 'blue', 'red', 'red'], s=100, label="Charges")
plt.legend()
plt.grid()
plt.show()

