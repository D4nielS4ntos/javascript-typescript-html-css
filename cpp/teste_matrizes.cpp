#include <iostream>
using namespace std;


void imprimeMatriz(int matriz[5][5]) {
    cout << "Matriz:\n";
    for (int l = 0; l < 5; ++l) {
        for (int c = 0; c < 5; ++c) {
            cout << "[ " << matriz[l][c] << " ] ";
        }
        cout << endl;
    }
}

int main() {
    int matriz[5][5] = {
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0}
    };
    int l, c;

    while (true) {

        imprimeMatriz(matriz);
    
        cout << "Digite uma coordenada (linha):\n";
        cin >> l;
        cout << "Digite uma coordenada (coluna):\n";
        cin >> c;
    
        if (l >= 0 && l < 5 && c >= 0 && c < 5) {
            matriz[l][c] += 1;
        } else {
            cout << "Coordenada fora dos limites da matriz." << endl;
        }

        system("cls || clear"); 

    }
    return 0;
}
