import numpy as np
import matplotlib.pyplot as plt

# Parameters
h = 0.01  # Step size
x_min = 0.1  # Avoid singularity at x=0
x_max = 0.99
n_steps = int((x_max - x_min) / h) + 1

# Theoretical solution: y = x * arccos(x)
def theoretical_solution(x):
    return x * np.arccos(x)

# Function for dy/dx
def dydx(x):
    return np.arccos(x) - (1 / np.sqrt(1 - x**2))

# Euler’s method
x_comp = [x_min]
y_comp = [0.0]  # Initial condition

for _ in range(n_steps):
    x_prev = x_comp[-1]
    y_prev = y_comp[-1]

    # Compute next values
    y_next = y_prev + h * dydx(x_prev)
    x_next = x_prev + h

    # Stop if values become invalid
    if x_next > x_max or np.isnan(y_next):
        break

    x_comp.append(x_next)
    y_comp.append(y_next)

# Convert lists to arrays
x_comp = np.array(x_comp)
y_comp = np.array(y_comp)

# Theoretical solution values for comparison
x_theory = np.linspace(x_min, x_max, 500)
y_theory = theoretical_solution(x_theory)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_theory, y_theory, label='Theoretical Solution (x * arccos(x))', color='blue', lw=2)
plt.plot(x_comp, y_comp, label="Euler's Method", color='red', linestyle='--', lw=2)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Solution using Euler’s Method vs Theoretical Solution', fontsize=16)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

