#include <stdio.h>
#include <math.h>

// Function representing dy/dx
double f(double x) {
    double denom = sqrt(fmax(1 - x * x, 1e-10)); // Prevent sqrt of negative values
    return acos(x) - (1 / denom);
}

// Runge-Kutta 4th order method to solve the differential equation
void rk4_method(double x0, double y0, double h, double x_max, double* results) {
    double x = x0;
    double y = y0;
    int i = 0;
    results[i] = y;
    
    while (x <= x_max) {
        // Compute the RK4 coefficients
        double k1 = h * f(x);
        double k2 = h * f(x + 0.5 * h);
        double k3 = h * f(x + 0.5 * h);
        double k4 = h * f(x + h);

        // Update the solution using RK4 formula
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4);
        x = x + h;  // Update x
        if (x > 0.99) break;  // Prevent singularity at x = 1
        i++;
        results[i] = y;
    }
}

