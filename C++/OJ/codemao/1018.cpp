#include <iostream>

int main() {
    // 定义变量以存储输入的整数
    int n;

    // 从输入中读取整数
    std::cin >> n;

    // 判断整数是否是3和7的倍数
    if (n % 3 == 0 && n % 7 == 0) {
        std::cout << n / 3 << std::endl;
        std::cout << n / 7 << std::endl;
    } else {
        std::cout << "no" << std::endl;
    }

    return 0;
}
