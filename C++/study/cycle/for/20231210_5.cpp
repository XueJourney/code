#include<iostream>
using namespace std;

int main(){
    int n;
    scanf("%d",n);
    int all,temp;
    for(int i=0;i<n;i++){
        cin>>temp;
        all+=temp;
    }
    int res = all/n;
    printf("%d.2f",res);
}