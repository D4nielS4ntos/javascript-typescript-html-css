#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


int main() {
    string text;
    char sub;
    char qualquer;
    
    cout << "Digite uma frase: " << endl;
    getline(cin, text);
    cout << "Digite um texto para procurar: " << endl;
    cin >> sub;
    cout << "Digite um texto para substituir: " << endl;
    cin >> qualquer;

    for (auto& c: text) {
        if (c == sub) {
            c = qualquer; // Replace with a placeholder or desired character
        }
    }

    cout << text;

    return 0;
}
