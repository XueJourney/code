#include <iostream>

int main() {
    // 定义变量以存储输入的整数
    int n;

    // 从输入中读取整数
    std::cin >> n;

    // 判断整数是奇数还是偶数
    if (n % 2 == 0) {
        std::cout << "even number" << std::endl;
    } else {
        std::cout << "Odd number" << std::endl;
    }

    return 0;
}
