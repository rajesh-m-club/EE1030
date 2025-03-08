# Given phi value (45 degrees -> π/4 radians)
phi_fixed = np.pi / 4

# Define s values from 0.1 to 5 (avoiding division by zero)
s = np.linspace(0.1, 5, 100)

# Compute F components
F_s = 40 / (s**2 + 1) + 3 * (np.cos(phi_fixed) + np.sin(phi_fixed))
F_phi = 3 * (np.cos(phi_fixed) - np.sin(phi_fixed))
F_z = -2

# Compute magnitude of F
F_magnitude = np.sqrt(F_s**2 + F_phi**2 + F_z**2)

# Plot the magnitude vs s
plt.figure(figsize=(7, 5))
plt.plot(s, F_magnitude, label=r'$|\mathbf{F}|$', color='r')
plt.xlabel(r'$s$')
plt.ylabel(r'$|\mathbf{F}|$')
plt.title(r'Magnitude of $\mathbf{F}$ as a function of $s$ for $\phi=45^\circ$')
plt.legend()
plt.grid()
plt.show()

