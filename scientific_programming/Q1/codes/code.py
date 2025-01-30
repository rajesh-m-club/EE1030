import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the shared library
euler_lib = ctypes.CDLL('./code.so')  # Use the appropriate file extension for your OS

# Define parameters
h = 0.01  # Step size
x_min = 0.1  # Avoid singularity at x=0
x_max = 0.99  # Stop before singularity at x=1
n_steps = int((x_max - x_min) / h) + 1

# Allocate memory for the results
results = (ctypes.c_double * n_steps)()

# Call the rk4_method function (formerly euler_method)
euler_lib.rk4_method(ctypes.c_double(x_min), ctypes.c_double(0.0), ctypes.c_double(h), ctypes.c_double(x_max), results)

# Convert results to numpy array for plotting
y_values = np.ctypeslib.as_array(results)

# Theoretical solution: y = x * arccos(x)
def theoretical_solution(x):
    return x * np.arccos(x)

# Theoretical solution for comparison
x_theory = np.linspace(x_min, x_max, 500)
y_theory = theoretical_solution(x_theory)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_theory, y_theory, label='Theoretical Solution (x * arccos(x))', color='blue', lw=2)
plt.plot(np.linspace(x_min, x_max, n_steps), y_values, label="RK4 Method", color='red', linestyle='--', lw=2)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title("Solution using RK4 Method vs Theoretical Solution", fontsize=16)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()

