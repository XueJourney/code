#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double result = fabs(pow(-5, 3) + 3) * pow(5, 2) / 16;
    
    // 输出结果，保留一位小数
    cout << fixed << setprecision(1) << result << endl;

    return 0;
}
