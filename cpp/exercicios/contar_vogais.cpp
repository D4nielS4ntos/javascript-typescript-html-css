#include <iostream>
#include <string>
using namespace std;


int main() {
    string text;
    cout << "Digite uma palavra: " << endl;
    cin >> text;
    string vogais = "AEIOU";
    int n = 0;

    for (auto t: text) {
        for (auto v: vogais) {
            if (tolower(t) == tolower(v)) {
                // cout << t << v << endl;
                n++;
            }
        }
    }
    cout << n;

    return 0;
}
