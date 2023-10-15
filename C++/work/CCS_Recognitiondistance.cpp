#include <iostream>
#include <cmath>
#include <limits>

int main() {
    // 定义m的取值范围和步长
    double start = -100;
    double end = 100;
    double step = 0.0000001;

    // 初始化最小“识别距离”和对应的m值
    double min_distance = std::numeric_limits<double>::infinity();
    double min_m = 0;

    // 对每个m值，计算“识别距离”
    for (double m = start; m <= end; m += step) {
        double x1 = m;
        double y1 = 3.0 / 4.0 * m + 3;  // 点C的坐标
        double x2 = 0;
        double y2 = 1;  // 点D的坐标

        // 计算“识别距离”
        double distance;
        if (std::abs(x1 - x2) >= std::abs(y1 - y2)) {
            distance = std::abs(x1 - x2);
        } else {
            distance = std::abs(y1 - y2);
        }

        // 如果当前“识别距离”小于已知的最小“识别距离”，则更新最小“识别距离”和对应的m值
        if (distance < min_distance) {
            min_distance = distance;
            min_m = m;
        }
    }

    // 输出最小“识别距离”和对应的m值
    std::cout << "最小“识别距离”为：" << min_distance << std::endl;
    std::cout << "对应的m值为：" << min_m << std::endl;

    return 0;
}
