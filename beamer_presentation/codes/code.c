#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to calculate the quadrant based on coordinates
const char* find_quadrant(double x, double y) {
    if (x > 0 && y > 0)
        return "First Quadrant";
    else if (x < 0 && y > 0)
        return "Second Quadrant";
    else if (x < 0 && y < 0)
        return "Third Quadrant";
    else if (x > 0 && y < 0)
        return "Fourth Quadrant";
    else if (x == 0 && y == 0)
        return "Origin";
    else if (x == 0)
        return "Y-Axis";
    else
        return "X-Axis";
}

int main() {
    // Points P (7, -6) and Q (3, 4)
    double x1 = 7, y1 = -6;
    double x2 = 3, y2 = 4;

    // Ratio m1 : m2 = 1 : 2
    double m1 = 1, m2 = 2;

    // Create matrices for P and Q
    int m = 2, n = 1;
    double **P = createMat(m, n);
    double **Q = createMat(m, n);
    P[0][0] = x1;
    P[1][0] = y1;
    Q[0][0] = x2;
    Q[1][0] = y2;

    // Calculate the point that divides PQ in the ratio 1:2 using Matadd and Matscale
    double **dividing_point = Matadd(Matscale(P, m, n, m2), Matscale(Q, m, n, m1), m, n);
    dividing_point[0][0] /= (m1 + m2);
    dividing_point[1][0] /= (m1 + m2);

    // Coordinates of the dividing point
    double x = dividing_point[0][0];
    double y = dividing_point[1][0];

    // Find the quadrant
    const char* quadrant = find_quadrant(x, y);

    // Write the result to a text file
    FILE *fptr = fopen("dividing_point.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fprintf(fptr, "The point that divides the line segment PQ in the ratio 1:2 is: (%lf, %lf)\n", x, y);
    fprintf(fptr, "The point lies in the: %s\n", quadrant);

    fclose(fptr);

    // Free allocated memory
    freeMat(P, m);
    freeMat(Q, m);
    freeMat(dividing_point, m);

    printf("Coordinates and quadrant successfully written to 'dividing_point.txt'\n");

    return 0;
}

