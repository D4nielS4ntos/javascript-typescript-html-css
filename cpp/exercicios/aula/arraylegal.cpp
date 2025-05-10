#include <iostream>
#include <vector>
#include <math.h>

int main() {
    int n;
    int el;
    bool legal = true;
    std::vector<int> arr = {};

    // std::cout << "digite o número: " << std::endl;
    std::cin >> n;

    for (int i=1; i<=n; i++) {
        // std::cout << "digite outro número" << std::endl;
        std::cin >> el;
        arr.push_back(el);
    }

    for (int e=1; e<=n-1; e++) {
        if (!((arr[e] - (arr[e-1])) % 2 == 0)) {
            legal = false;
        }
    }

    (legal) ? std::cout << "Legal" : std::cout << "Chato";
}
