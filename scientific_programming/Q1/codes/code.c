#include <stdio.h>
#include <math.h>

// Function representing dy/dx
double f(double x) {
    return acos(x) - (1 / sqrt(1 - x * x));
}

// Euler's method to solve the differential equation
void euler_method(double x0, double y0, double h, double x_max) {
    double x = x0;
    double y = y0;
    printf("x, y\n");
    while (x <= x_max) {
        printf("%lf, %lf\n", x, y);
        y = y + h * f(x);  // Euler's method step
        x = x + h;         // Update x
    }
}

int main() {
    // Parameters
    double h = 0.01;   // Step size
    double x_min = 0.1; // Initial x value (to avoid singularity at 0)
    double x_max = 1.0; // Maximum x value
    double y0 = 0.0;    // Initial condition

    euler_method(x_min, y0, h, x_max);

    return 0;
}

