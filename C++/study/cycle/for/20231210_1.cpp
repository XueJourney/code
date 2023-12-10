#include<iostream>
using namespace std;

int main(){
    for(int i=1;i<=9;i++){
        for(int j=1;j<=9;j++){
            for(int k=1;k<=9;k++){
                if(i*100+j*10+k==i*i*i+j*j*j+k*k*k){
                    cout<<i*100+j*10+k<<endl;
                }
            }
        }
    }
}