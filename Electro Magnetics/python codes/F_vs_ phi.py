import numpy as np
import matplotlib.pyplot as plt

# Constants
s_fixed = 3  # Given s-value for (a)

# Define phi values from 0 to 2π
phi = np.linspace(0, 2 * np.pi, 100)

# Compute F components
F_s = 40 / (s_fixed**2 + 1) + 3 * (np.cos(phi) + np.sin(phi))
F_phi = 3 * (np.cos(phi) - np.sin(phi))
F_z = -2

# Compute magnitude of F
F_magnitude = np.sqrt(F_s**2 + F_phi**2 + F_z**2)

# Plot the magnitude vs phi
plt.figure(figsize=(7, 5))
plt.plot(phi, F_magnitude, label=r'$|\mathbf{F}|$', color='b')
plt.xlabel(r'$\phi$ (radians)')
plt.ylabel(r'$|\mathbf{F}|$')
plt.title(r'Magnitude of $\mathbf{F}$ as a function of $\phi$ for $s=3$')
plt.legend()
plt.grid()
plt.show()

