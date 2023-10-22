#include <iostream>
#include <iomanip> // 用于设置输出格式
using namespace std;

int main() {
    // 声明变量用于存储作业成绩、小测成绩和期末考试成绩
    double homework_score, quiz_score, final_exam_score;

    // 输入作业成绩、小测成绩和期末考试成绩
    cin >> homework_score >> quiz_score >> final_exam_score;

    // 计算最终成绩
    double final_score = homework_score * 0.2 + quiz_score * 0.3 + final_exam_score * 0.5;

    // 输出最终成绩，保留一位小数
    cout << fixed << setprecision(1) << final_score << endl;

    return 0;
}
