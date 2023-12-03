#include<iostream>
using namespace std;

int fac(int);

int main()
{
	int n;
	while(n=15)
	{
		cout<<n<<"!= "<<fac(n)<<endl;
	}
	return 0;
}

int fac(int x)
{
	register int i,f=1;  //定义寄存器变量
	for(i=1;i<=x;i++)
		f*=i;
	return f;
}