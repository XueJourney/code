#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <random>
#include <chrono>
#include <cmath>
#include <iterator>
#include <functional>
#include <thread>

int main() {
    // 使用vector存储数据
    std::vector<int> vec(10);
    std::iota(vec.begin(), vec.end(), 1); // 填充1到10

    // 使用map作为键值对存储
    std::map<std::string, int> wordCount;
    wordCount["hello"] = 1;
    wordCount["world"] = 2;

    // 使用set存储唯一元素
    std::set<int> uniqueNumbers(vec.begin(), vec.end());

    // 使用algorithm对数据进行操作
    std::sort(vec.begin(), vec.end(), std::greater<int>());

    // 使用random生成随机数
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(1, 100);

    // 使用chrono处理时间
    // auto start = std::chrono::high_resolution_clock::now();
    // std::this_thread::sleep_for(std::chrono::seconds(1));
    // auto end = std::chrono::high_resolution_clock::now();
    // std::chrono::duration<double> diff = end - start;

    // 输出结果
    // std::cout << "Vector sorted in reverse order: ";
    // for (int n : vec) std::cout << n << ' ';
    // std::cout << "\nRandom number: " << distrib(gen);
    // std::cout << "\nElapsed time: " << diff.count() << " s\n";

    // 使用cmath进行数学运算
    std::cout << "Square root of 16 is " << std::sqrt(16) << std::endl;

    return 0;
}
