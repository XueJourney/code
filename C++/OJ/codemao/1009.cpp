#include <iostream>
#include <iomanip> // 用于格式化输出

using namespace std;

int main() {
    int n;
    cin >> n; // 输入钱的张数

    int totalMoney = n * 10; // 计算总钱数
    double pencilPrice = 0.45;
    int maxPencils = totalMoney / pencilPrice; // 计算最多能买多少支铅笔

    double leftMoney = totalMoney - maxPencils * pencilPrice; // 计算剩下的钱

    // 输出结果
    cout << "buy=" << maxPencils << endl;
    cout << "left=" << fixed << setprecision(1) << leftMoney << endl;
    cin.ignore();
    return 0;
}
