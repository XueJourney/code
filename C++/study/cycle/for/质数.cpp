#include <iostream>
using namespace std;

int main(){
	int a;
	cin >> a;
//	a = 172;
	int res = 0;
	for(int i=1;i<=a;i++){
		if((a % i)== 0){
			res++;
		}
	}
	if(res==2){
		cout << "ture" << endl;
	}else{
		cout << "false" << endl;
	}
}
