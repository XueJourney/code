# include <iostream>
# include <list>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0, threes = 0;

        for (int num : nums) {
            twos |= (ones & num);
            ones ^= num;
            threes = ones & twos;

            if (threes != 0) {
                ones &= ~threes;
                twos &= ~threes;
            }
        }

        return ones;
    }
};