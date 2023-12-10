#include<iostream>
using namespace std;

int main(){
    int f,i,j;
    scanf("%d %d %d",&f,&i,&j);
    // f = 3;
    // i = 4;
    // j = 3;
    for(int k=0;k<i;k++){
        cout<<f+k*j<<" ";
    }
}