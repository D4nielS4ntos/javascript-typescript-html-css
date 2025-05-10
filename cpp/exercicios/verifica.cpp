#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main() {
    vector<string> vetor = {"caixa", "baixa", "carga", "larga", "deixa"};
    string palavra;
    bool estar = false;

    cout << "Digite uma palavra para descobrir se está na lista: " << endl;
    cin >> palavra;
    for (auto i: vetor) {
        if (i == palavra) {
            estar = true;
            break;
        }
    }
    
    (estar) ? cout << "Tá dentro" << endl : cout << "Não tá dentro" << endl;

    return 0;
}
