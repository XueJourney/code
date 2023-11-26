#include <iostream>
using namespace std;

int square(int num){
    return num*num;
}

int main(){
    int num;
    scanf("%d",&num);
    // num =5;
    printf("%d %d %d",8,(num-2)*12,square(num-2)*6);
}