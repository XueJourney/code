#include <iostream>
#include <cmath>  // 引入cmath库以使用round函数

int main() {
    // 定义变量以存储输入的值
    double x, a, b, c, d;

    // 从输入中读取值
    std::cin >> x >> a >> b >> c >> d;

    // 计算多项式的值
    double y = a * pow(x, 3) + b * pow(x, 2) + c * x + d;

    // 对y进行四舍五入
    int result = round(y);

    // 输出结果
    std::cout << result << std::endl;

    return 0;
}
