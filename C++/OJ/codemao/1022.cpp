#include <iostream>
#include <iomanip>

using namespace std; // 使用std命名空间

// 计算车费的函数
float calculateFare(float distance) {
    const float baseFare = 13.0f; // 起步价
    const float baseDistance = 3.0f; // 起步里程
    const float additionalRate = 2.3f; // 超出起步里程的单价

    // 如果车程在3公里及以内，直接返回起步价
    if (distance <= baseDistance) {
        return baseFare;
    } else {
        // 否则，计算超出部分的费用
        float extraDistance = distance - baseDistance;
        float extraFare = extraDistance * additionalRate;
        return baseFare + extraFare;
    }
}

int main() {
    float distance;
    cin >> distance;

    float fare = calculateFare(distance);
    
    // 设置输出的精度（小数点后一位）
    cout << fare << endl;

    return 0;
}
