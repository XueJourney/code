# include <iostream>
#include <windows.h>
using namespace std;

int main(){
    SetConsoleOutputCP(CP_UTF8);
    char standard;
    standard = 'A';
    int num;
    num = 23;
    long long count;
    count = 10000000000;
    float price;
    price = 13.4;
    double value;
    value = 3.14159265358979323846264338327950288419716939937510582097494459230;
    printf("这道题答案是%c选项\n",standard);
    printf("我今天买了%d个苹果\n",num);
    printf("这本书一共有%ld页\n",count);
    printf("这本书的价格为%f元\n",price);
    printf("圆周率的取值:%lf\n",value);
    system("pause");
    return 0;
}
