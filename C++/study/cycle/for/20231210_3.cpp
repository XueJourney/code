#include<iostream>
using namespace std;

int main(){
    int i;
    cin >> i;
    for(;i!=1;){
        if(i%2==0){
            cout<<i<<endl;
            i/=2;
        }else{
            i=3*i+1;
        }
    }
    cout<<"Done"<<endl;
}