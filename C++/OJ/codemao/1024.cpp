#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int totalCost;
    if (n <= 5) {
        totalCost = n * 300; // 5人及以下，每人300元
    } else {
        totalCost = n * 280; // 超过5人，每人280元
    }

    cout << totalCost << endl;

    return 0;
}
