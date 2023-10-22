#include <iostream>
using namespace std;

int main() {
    // 声明两个整数变量a和b
    int a, b;

    // 输入两个整数
    cin >> a >> b;

    // 使用一个额外的变量temp来进行交换
    int temp = a;
    a = b;
    b = temp;

    // 输出交换后的值
    cout << a << " " << b << endl;

    return 0;
}
