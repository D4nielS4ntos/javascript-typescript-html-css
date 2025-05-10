#include <iostream>
#include <string>
using namespace std;


int main() {
    string text;
    cout << "Digite uma palavra: " << endl;
    cin >> text;

    (text == string(text.rbegin(), text.rend())) ? cout << "é palindromo" : cout << "não é palindromo";

    return 0;
}
