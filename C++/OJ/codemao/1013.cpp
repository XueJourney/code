#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // 声明变量来存储高度和半径
    int h, r;

    // 输入高度和半径
    cin >> h >> r;

    // 计算每个小圆桶的容积
    double bucket_volume = 3.14159 * pow(r, 2) * h;

    // 计算所需的桶数，并向上取整
    int buckets_needed = ceil(20.0 / bucket_volume);

    // 输出结果
    cout << buckets_needed << endl;

    return 0;
}
