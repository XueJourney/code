#include <iostream>
using namespace std;

int main(){
	int a,b,c;
//	scanf("%d %d %d",a,b,c);
	cin >> a >> b >> c;
	printf("%d %d %d\n",a,b,c);
	for(int x =1;x<a;++x){
//		printf("%d",x);
		if(a%x == b%x && b%x == (c%x)){
			printf("%d",x);
		}
	}
}
