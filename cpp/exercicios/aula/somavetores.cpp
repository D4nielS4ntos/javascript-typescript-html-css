#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int A[n], B[n], C[n], soma[n];


    for (int i=0; i<=n-1; i++) {
        cin >> A[i];
    }
    for (int i=0; i<=n-1; i++) {
        cin >> B[i];
    }
    for (int i=0; i<=n-1; i++) {
        cin >> C[i];
    }

    for (int j=0; j<=n-1; j++) {
        soma[j] = A[j] + B[j] + C[j];
    }

    for (int e : soma) cout << e << " ";
}
