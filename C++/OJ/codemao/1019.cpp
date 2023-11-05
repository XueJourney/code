#include <iostream>
using namespace std;

int main(){
    float weight, tall;  // 将tall的数据类型更改为float
    cin >> tall;
    cin >> weight;
    float bmi;
    bmi = weight / (tall * tall);
    cout << bmi<< endl;
    if(bmi < 18.5){
        cout << "Thin" << endl;
    } else if (18.5 <= bmi && bmi <= 24){
        cout << "Normal" << endl;
    } else{
        cout << "Fat" << endl;
    }
}
