#include <iostream>
using namespace std;

// 函数声明
unsigned long long factorial(unsigned int n);

int main() {
    unsigned int n;
    cout << "Enter a positive integer: ";
    cin >> n;

    cout << n << "! = " << factorial(n) << endl;
    return 0;
}

// 函数定义
unsigned long long factorial(unsigned int n) {
    if (n == 0) return 1; // 0的阶乘是1
    return n * factorial(n - 1); // 递归计算阶乘
}
