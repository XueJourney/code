#include <iostream>
using namespace std;

int main() {
    int n = 6;
    int result = 1;
    for(int i=1; i<n-1 ;i++){
        result = result * (i+1);
    }
    cout << result << endl;
}