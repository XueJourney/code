#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int a,b,c,d;
    scanf("%d %d %d",&a,&b,&c);
    d = ceil(c/b);
    if(d<a){
        printf("剩下%.0f个苹果",a-c);
    }else{
        printf("没有苹果了");
    }
    return 0;
}