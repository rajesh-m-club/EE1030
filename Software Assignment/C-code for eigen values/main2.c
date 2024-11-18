#include <stdio.h>
#include <math.h>

#define N 10

void multiply_matrices(double A[N][N], double B[N][N], double result[N][N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void transpose(double matrix[N][N], double result[N][N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = matrix[j][i];
        }
    }
}
void subtract_matrices(double A[N][N], double B[N][N], double result[N][N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = A[i][j] - B[i][j];
        }
    }
}

double norm(double matrix[N][N], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum += matrix[i][j] * matrix[i][j];
        }
    }
    return sqrt(sum);
}

void qr_decompose(double A[N][N], double Q[N][N], double R[N][N], int n) {
    double temp[N];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            Q[i][j] = 0;
            R[i][j] = 0;
        }
    }

    for (int j = 0; j < n; j++) {
        double norm_col = 0;
        for (int i = 0; i < n; i++) {
            norm_col += A[i][j] * A[i][j];
        }
        R[j][j] = sqrt(norm_col);

        for (int i = 0; i < n; i++) {
            Q[i][j] = A[i][j] / R[j][j];
        }

        for (int k = j + 1; k < n; k++) {
            double dot_product = 0;
            for (int i = 0; i < n; i++) {
                dot_product += A[i][k] * Q[i][j];
            }
            R[j][k] = dot_product;

            for (int i = 0; i < n; i++) {
                A[i][k] -= Q[i][j] * R[j][k];
            }
        }
    }
}

void qr_algorithm(double matrix[N][N], int n, int max_iterations) {
    double A[N][N], Q[N][N], R[N][N], A_new[N][N];
    double eigenvalues[N];
    int iteration = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = matrix[i][j];
        }
    }

    while (iteration < max_iterations) {
        qr_decompose(A, Q, R, n);

        multiply_matrices(R, Q, A_new, n);

        if (norm(A_new, n) < 1e-6) {
            break;
        }


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = A_new[i][j];
            }
        }

        iteration++;
    }

    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A[i][i];
    }

    printf("Eigenvalues:\n");
    for (int i = 0; i < n; i++) {
        printf("%lf ", eigenvalues[i]);
    }
    printf("\n");
}

int main() {
    int n = 3;
    double matrix[N][N] = {{6, 2, 1},
                           {2, 5, 3},
                           {1, 3, 4}};
    int max_iterations = 1000;

    qr_algorithm(matrix, n, max_iterations);

    return 0;
}
