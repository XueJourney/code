# include <iostream>
using namespace std;

int main(){
    // 三行三个整数，分别表示时分秒
    int hour, minute, second;
    cin >> hour;
    cin >> minute;
    cin >> second;
    // 将所有数据转为秒并相加
    int sum = hour * 3600 + minute * 60 + second;
    // 输出
    cout << sum;
    return 0;
}