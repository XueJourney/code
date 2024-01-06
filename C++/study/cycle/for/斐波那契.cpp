#include <iostream>
using namespace std;

int main(){
	int k,a,b,c;
	cin >> k;
	a = 1;
	b = 1;
	for(int i=3;i<=k;i++){
		c= a + b;
		printf("%d ",c);
		a = b;
		b = c;
	}
}
