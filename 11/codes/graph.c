#include <stdio.h>
#include <math.h>

double geometric_sum(int n, double a, double r) {
    return a * ((pow(r, n + 1) - 1) / (r - 1));
}

int main() {
    // Geometric progression parameters
    double a = 0.15;
    double r = 0.1;
    int n_terms = 20;

    // Open file for writing
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the calculated values to the file
    for (int n = 0; n <= n_terms; ++n) {
        double sum = geometric_sum(n, a, r);
        fprintf(file, "%d %f\n", n, sum);
    }

    // Close the file
    fclose(file);

    return 0;
}

