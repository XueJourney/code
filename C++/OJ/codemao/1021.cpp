#include <iostream>
using namespace std;

char getGrade(int score) {
    if (score >= 90) return 'A';
    else if (score >= 70) return 'B';
    else if (score >= 60) return 'C';
    else return 'D';
}

int main() {
    int score;
    cin >> score;


    char grade = getGrade(score);
    cout << grade << endl;

    return 0;
}
