#include <iostream>
using namespace std;

int main(){
	int all_person = 35;
	int all_steamed_bread = 94;
	for(int i=0;i<all_person;i++){
		int steamed_bread = i*4+(35-i)*2;
		if (steamed_bread == all_steamed_bread){
			printf("%d %d",i,(35-i));
		}
	}
}
