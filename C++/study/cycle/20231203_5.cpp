#include <iostream>
#include <cmath>

using namespace std;

bool isNarcissistic(int num) {
    int originalNum = num;
    int sum = 0;
    int numDigits = to_string(num).length();

    while (num > 0) {
        int digit = num % 10;
        sum += pow(digit, numDigits);
        num /= 10;
    }

    return sum == originalNum;
}

int main() {
    cout << "水仙花数（100-1000）：" << endl;

    for (int i = 100; i <= 1000; i++) {
        if (isNarcissistic(i)) {
            cout << i << " ";
        }
    }

    cout << endl;
    return 0;
}