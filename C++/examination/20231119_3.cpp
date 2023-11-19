#include <iostream>
using namespace std;

int main(){
    float tall,money;
    // scanf("%f %f",&tall,&money);
    tall = 1.25;
    money = 520;
    if(tall>=1.2 && tall<=1.5){
        printf("%f",money*0.5);
    }else if (tall>=1.5);{
        printf("%f",&money);
    }
}