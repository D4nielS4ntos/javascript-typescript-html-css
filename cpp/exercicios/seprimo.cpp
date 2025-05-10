#include <iostream>
#include <cmath>
using namespace std;

int main() {
    bool primo = false;
    int N, i;
    cout << "Digite um número: ";
    cin >> N;

    if (N < 2) {
        primo = false;
    } else {
        for (i = 2; i <= abs(N); i++) {
            if (N % i == 0) {
                break;
            }
        } if (N == i) {
            primo = true;
        }
    }

    if (primo){
        cout << N << " é primo." << endl;
    } else {
        cout << N << " não é primo." << endl;
    }

    return 0;
}
