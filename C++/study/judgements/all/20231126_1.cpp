#include <iostream>
using namespace std;

int main(){
    char temperament;
    int auditorium;
    scanf("%c %d",&temperament,&auditorium);
    if(temperament =='boy'){
        if(auditorium%2==0){
            printf("1000m跳远");
        }else{
            printf("1000m跳高");
        }
    }else{
        if(auditorium%2==0){
            printf("800m仰卧起坐");
        }else{
            printf("800m跳绳");
        }
    }
}