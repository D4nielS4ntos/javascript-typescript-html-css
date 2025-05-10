#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;


int main() {
    string text;
    cout << "Digite uma frase: " << endl;
    getline(cin, text);

    vector<string> tokens;
    istringstream iss(text);
    string token;
    
    while (getline(iss, token, ' ')) {  // Divide por espaços
        if (!token.empty()) {  // Ignora tokens vazios
            tokens.push_back(token);
        }
    }

    // Novo texto
    string textNew;
    for (auto t: tokens) {
        t[0] = toupper(t[0]);

        //t = t[0] + " ";
        textNew += t+" ";
    };

    text = textNew;
    cout << text;

    return 0;
}
