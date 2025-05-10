#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


int main() {
    string text;
    int N = 0;
    cout << "Digite uma frase: " << endl;
    getline(cin, text);

    vector<string> tokens;
    istringstream iss(text);
    string token;
    
    while (getline(iss, token, ' ')) {  // Divide por espaços
        if (!token.empty()) {  // Ignora tokens vazios
            N++;
        }
    }

    cout << "N° de palavras: " << N;

    return 0;
}
