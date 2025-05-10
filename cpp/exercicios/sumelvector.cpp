#include <iostream>
#include <vector>
using namespace std;


int main() {
    vector<int> a = {2,0,3};
    int sum = 0;

    for (int i: a) {
        sum += i;
    }

    cout << "Soma dos termos: " << sum;

    return 0;
}
