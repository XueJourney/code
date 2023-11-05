#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<std::vector<int>> triangle(n, std::vector<int>(n, 0));

    // Read the input for the triangle
    for (int i = 0; i < n; ++i)
        for (int j = 0; j <= i; ++j)
            std::cin >> triangle[i][j];

    // Start from the second to last row and move upwards
    for (int i = n - 2; i >= 0; --i) {
        for (int j = 0; j <= i; ++j) {
            // Update the maximum sum of paths starting at the current cell
            triangle[i][j] += std::max(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }

    // The top element now contains the maximum sum
    std::cout << triangle[0][0] << std::endl;

    return 0;
}
