#include <iostream>
using namespace std;

int main(){
    int weight,tall;
    weight = 50;
    tall = 1.8;
    float bmi;
    bmi = weight / (tall * tall);
    cout << "BMI is " << bmi << endl;
    if(bmi < 18.5){
        cout << "Underweight" << endl;
    } else if (18.5 <= bmi && bmi <= 24){
        cout << "Normal weight" << endl;
    } else{
        cout << "Overweight" << endl;
    }
}