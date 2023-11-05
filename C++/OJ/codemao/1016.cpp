#include <iostream>

int main() {
    // 定义变量以存储输入的整数
    int n;

    // 从输入中读取整数
    std::cin >> n;

    // 判断是否为偶数
    if (n % 2 == 0) {
        std::cout << "yes" << std::endl;
    }

    return 0;
}
