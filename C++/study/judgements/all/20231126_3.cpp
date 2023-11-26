#include <iostream>
using namespace std;

int main(){
    int a,b,c,d;
    scanf("%d %d %d",&a,&b,&c);
    if(c%b==0){
        d=c/b;
    }else{
        d=c/b+1;
    }
    printf("%d",a-d);
    return 0;
}