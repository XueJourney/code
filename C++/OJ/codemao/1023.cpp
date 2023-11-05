#include <iostream>

using namespace std;

// 判断闰年的函数
bool isLeapYear(int year) {
    // 如果年份能被400整除，则是闰年（世纪闰年）
    if (year % 400 == 0) return true;
    // 否则，如果年份能被4整除但不能被100整除，则是闰年（普通闰年）
    if (year % 4 == 0 && year % 100 != 0) return true;
    // 其他的都不是闰年
    return false;
}

int main() {
    int year;
    cin >> year;

    // 检查输入是否合理，年份应该是一个正整数
    if (year <= 0) {
        cout << "输入的年份不合理，请输入一个正整数年份。" << endl;
        return 1;
    }

    // 判断并输出结果
    if (isLeapYear(year)) {
        cout << "leap year" << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}
