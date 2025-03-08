import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

# Compute Potential at each point
V = np.zeros(X.shape)

for q, (qx, qy) in charges:
    r = np.sqrt((X - qx) ** 2 + (Y - qy) ** 2)
    r[r == 0] = 1e-9  # Prevent division by zero
    V += k * q / r

# Plotting the potential as a 3D surface
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V, cmap='plasma')

ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("Potential (V)")
ax.set_title("Electric Potential Surface Plot")
plt.show()

