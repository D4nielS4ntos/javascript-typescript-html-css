#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;


int main() {
    // media = sizeof(blabla) / sizeof(blabla.at(0));
    vector<int> vetor = {12, 43, 12, 54, 32, 12, 122};
    int sum = 0;
    float somatorio = 0;

    for (int i: vetor) {
        sum += i;
    }

    float media = sum / vetor.size();

    // cout << sum << endl;
    // cout << media << endl;

    for (int i: vetor) {
        somatorio += pow((i - media), 2);
    }
    float dp = sqrt(somatorio / vetor.size());
    cout << "O desvio padrão é igual a: " << dp << endl;

    return 0;
}
