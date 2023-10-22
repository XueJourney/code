#include <iostream>
using namespace std;

int main() {
    // 声明变量用于存储摄氏温度和华氏温度
    double celsius, fahrenheit;

    // 输入摄氏温度
    cin >> celsius;

    // 使用公式将摄氏温度转换为华氏温度
    fahrenheit = (9.0/5.0) * celsius + 32;

    // 输出华氏温度
    cout << fahrenheit << endl;

    return 0;
}
