#include <iostream>
using namespace std;

int main(){
    int num_a, num_b;
    scanf("%d %d", &num_a, &num_b);
    // num_a = 9;
    // num_b = 4;
    int result;
    if(num_a % num_b == 0){
        result = num_a / num_b;
    }else if (num_a % num_b != 0){
        result = num_a / num_b + 1;
    }
    printf("%d", result);
}