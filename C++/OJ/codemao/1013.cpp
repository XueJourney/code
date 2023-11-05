#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // 声明变量来存储高度和半径
    int h, r;
    // 输入高度和半径
    cin >> h >> r;
    // 圆周率
    float pi;
    pi = 3.14159;
    // 计算水的体积
    float volume;
    volume = pi * r * r * h;
    int res;
    res = ceil(20 / (volume/1000));
    cout << res;

    return 0;
}
