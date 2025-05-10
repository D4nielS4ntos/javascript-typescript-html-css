#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, nPE, nPD;
    nPE = 0, nPD = 0;

    while (n > 20) {
        cin >> n;
    }

    int arr[n] = {};
    
    for (int i=0; i<=n-1; i++) {
        cin >> arr[i];
    }
    
    // direita
    for (int x=0; x<=n-1; x++) {
        (arr[x] == 1) && nPE++;
        if (arr[x] == 2) break;
    }
    // esquerda
    reverse(arr, arr+n);
    for (int x=0; x<=n-1; x++) {
        (arr[x] == 1) && nPD++;
        if (arr[x] == 2) break;
    }

    
    if (nPD > nPE) {
        cout << "esquerda";
    } else if (nPD < nPE) {
        cout << "direita";
    } else if (nPD == nPE) {
        cout << "tanto faz";
    }

    return 0;
}
