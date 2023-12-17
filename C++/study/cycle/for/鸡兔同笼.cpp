#include <iostream>
using namespace std;

int main(){
	int all_head = 35;
	int all_foot = 94;
	for(int i=0;i<all_head;i++){
		int foot = i*4+(35-i)*2;
		if (foot == all_foot){
			printf("%d %d",i,(35-i));
		}
	}
}
