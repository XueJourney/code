#include <iostream>
#include <chrono>
#include <ctime>

using namespace std;
using namespace chrono;

int main() {
    // 获取当前日期
    auto current_time = system_clock::now();
    time_t tt = system_clock::to_time_t(current_time);
    tm local_time = *localtime(&tt);

    // 计算星期几
    int today = local_time.tm_wday; // 星期天是0，星期一是1，依此类推

    // 获取用户输入
    int n;
    printf("请输入天数:");
    scanf("%d", &n);
    // n = 17;

    // 计算未来的星期几
    int futureDay = (today + n) % 7;

    // 输出结果
    // cout << n << " 天后是星期 " << futureDay << "(星期天是0,星期一是1,依此类推)" << endl;
    switch (n)
    {
    case 1:
        cout << n << "天后是星期一" << endl;
        break;
    case 2:
        cout << n << "天后是星期二" << endl;
        break;
    case 3:
        cout << n << "天后是星期三" << endl;
        break;
    case 4:
        cout << n << "天后是星期四" << endl;
        break;
    case 5:
        cout << n << "天后是星期五" << endl;
        break;
    case 6:
        cout << n << "天后是星期六" << endl;
        break;
    case 7:
        cout << n << "天后是星期日" << endl;
        break;
    default:
        cout << "输入的数字不代表一周内的某一天" << endl;
        break;
    }

    return 0;
}
