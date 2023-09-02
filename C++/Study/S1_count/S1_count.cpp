#include <iostream>
#include<ctime>
#include<stdlib.h>
using namespace std;

int main()
{
    int num_a, num_b, input_c;
    srand(time(0));
    num_a = rand() % 100;
    num_b = rand() % 100;
    // cout << num_a << "," << num_b;
    cin >> input_c;
    return 0;
}
